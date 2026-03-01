# This class prints a nice report back to the user.
class Presenter:
    @staticmethod
    def show_results(result: DecisionResult):
        # Header for the table
        print(f"\n{'='*60}")
        print(f" DECISION REPORT: {result.domain.upper()}")
        print(f"{'='*60}")
        
        header = f"{'Rank':<5} {'Option':<20} {'Score':<10}"
        print(header)
        print("-" * len(header))
        
        for res in result.results:
            if not res.is_eligible:
                status = "EXCLUDED"
                score_str = "N/A"
            else:
                status = str(res.rank)
                score_str = f"{res.total_score:.4f}"
            
            row = f"{status:<5} {res.name:<20} {score_str:<10}"
            print(row)
            
        print(f"\n{'EXPLANATION':<20}")
        print("-" * 20)
        
        # Show detail for top eligible options
        scored_results = [r for r in result.results if r.is_eligible]
        for res in scored_results[:2]: 
            print(f"\nWhy {res.name} (Rank {res.rank}):")
            for b in res.breakdown:
                print(f"  - {b.criterion:<15} : Raw={b.raw_value:>8} | Norm={b.normalized_value:>5.2f} | Weighted={b.weighted_score:>5.2f}")
        
        # Show why things were excluded
        ineligible = [r for r in result.results if not r.is_eligible]
        if ineligible:
            print(f"\n{'EXCLUSIONS':<20}")
            print("-" * 20)
            for res in ineligible:
                print(f"  - {res.name:<20} : {res.reason}")
        
        print(f"\n{'='*60}\n")
