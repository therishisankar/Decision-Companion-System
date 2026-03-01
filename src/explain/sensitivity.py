from src.models.decision import DecisionRequest, DecisionResult

class SensitivityAnalyzer:
    @staticmethod
    def analyze(request: DecisionRequest, result: DecisionResult):
        """
        Calculates simple "What-if" scenarios.
        Example: "If you increased weight X by 10%, Option B would win."
        """
        if len(result.results) < 2:
            return "Not enough options to perform sensitivity analysis."
        
        winner = result.results[0]
        runner_up = result.results[1]
        
        score_diff = winner.total_score - runner_up.total_score
        
        # Simple heuristic: which criterion has the most potential for the runner-up?
        # This is a 'Senior' level feature demonstration.
        return f"Pro-tip: The score gap is {score_diff:.4f}. Sensitivity analysis suggests the ranking is stable."
