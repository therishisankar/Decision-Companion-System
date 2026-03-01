from typing import List, Dict
from src.models.decision import DecisionRequest, DecisionResult, OptionResult, ScoreBreakdown
from src.core.normalizer import Normalizer

class Scorer:
    def __init__(self, request: DecisionRequest):
        self.request = request
        self.normalizer = Normalizer()

    def score(self) -> DecisionResult:
        # Step 1: Get rid of things that are too expensive
        results = []
        eligible_options = []
        
        for option in self.request.options:
            is_eligible = True
            reason = None
            
            if self.request.constraints:
                for criterion_name, limit in self.request.constraints.items():
                    val = option.values.get(criterion_name)
                    if val is not None:
                        # If the criterion is marked as 'is_cost', val must be <= limit
                        # This is a bit simplistic; ideally we'd check if the criterion exists
                        # For this demo, we assume if it's in constraints, it's a "Must be at most" or equality
                        if isinstance(val, (int, float)) and val > limit:
                            is_eligible = False
                            reason = f"{criterion_name} ({val}) exceeds limit ({limit})"
                            break
            
            if is_eligible:
                eligible_options.append(option)
            else:
                results.append(OptionResult(
                    name=option.name,
                    total_score=0.0,
                    rank=999,
                    breakdown=[],
                    is_eligible=False,
                    reason=reason
                ))
        
        # Step 2: Compare all the options that are left
        stats = self._get_criteria_stats(eligible_options)
        
        for option in eligible_options:
            total_score = 0.0
            breakdown = []
            
            for cri in self.request.criteria:
                raw_val = option.values.get(cri.name, 0.0)
                if not isinstance(raw_val, (int, float)):
                    raw_val = 0.0 
                
                min_v, max_v = stats[cri.name]
                norm_val = self.normalizer.scale(raw_val, min_v, max_v, cri.is_cost)
                weighted = norm_val * cri.weight
                
                total_score += weighted
                breakdown.append(ScoreBreakdown(
                    criterion=cri.name,
                    raw_value=float(raw_val),
                    normalized_value=norm_val,
                    weighted_score=weighted
                ))
            
            results.append(OptionResult(
                name=option.name,
                total_score=total_score,
                rank=0,
                breakdown=breakdown
            ))
            
        # Step 3: Sort them so the winner is at the top
        scored_results = [r for r in results if r.is_eligible]
        scored_results.sort(key=lambda x: x.total_score, reverse=True)
        
        for i, res in enumerate(scored_results):
            res.rank = i + 1
            
        return DecisionResult(domain=self.request.domain, results=results)

    def _get_criteria_stats(self, options: List[Option]) -> Dict[str, tuple]:
        stats = {}
        for cri in self.request.criteria:
            vals = [opt.values.get(cri.name, 0.0) for opt in options if isinstance(opt.values.get(cri.name), (int, float))]
            if not vals:
                stats[cri.name] = (0.0, 0.0)
            else:
                stats[cri.name] = (min(vals), max(vals))
        return stats
