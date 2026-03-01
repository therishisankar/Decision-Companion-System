import sys
import os
from src.io.parser import Parser
from src.core.scorer import Scorer
from src.io.presenter import Presenter
from src.explain.sensitivity import SensitivityAnalyzer

def main():
    if len(sys.argv) < 2:
        print("Usage: python src/cli.py <path_to_decision_json>")
        return

    filepath = sys.argv[1]
    if not os.path.exists(filepath):
        print(f"Error: File {filepath} not found.")
        return

    try:
        request = Parser.load_file(filepath)
        scorer = Scorer(request)
        result = scorer.score()
        
        Presenter.show_results(result)
        
        # Explainability Layer: What-if
        analysis = SensitivityAnalyzer.analyze(request, result)
        print(f"ANALYSIS: {analysis}\n")
    except Exception as e:
        print(f"System Error: {e}")

if __name__ == "__main__":
    main()
