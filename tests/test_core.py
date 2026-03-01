import sys
import os
sys.path.append(os.getcwd())

from src.models.decision import DecisionRequest, Criterion, Option
from src.core.scorer import Scorer

def test_basic_scoring():
    # Setup
    criteria = [
        Criterion(name="Cost", weight=0.5, is_cost=True),
        Criterion(name="Performance", weight=0.5, is_cost=False)
    ]
    options = [
        Option(name="AWS", values={"Cost": 100, "Performance": 80}),
        Option(name="GCP", values={"Cost": 80, "Performance": 90}),
    ]
    request = DecisionRequest(domain="Cloud", criteria=criteria, options=options)
    
    # Execute
    scorer = Scorer(request)
    result = scorer.score()
    
    # Verify
    print(f"Domain: {result.domain}")
    for res in result.results:
        print(f"Rank {res.rank}: {res.name} (Score: {res.total_score:.2f})")
        for b in res.breakdown:
            print(f"  - {b.criterion}: {b.raw_value} (Norm: {b.normalized_value:.2f})")

if __name__ == "__main__":
    test_basic_scoring()
