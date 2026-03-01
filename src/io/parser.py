import json
from typing import List, Dict
from src.models.decision import DecisionRequest, Criterion, Option

# This part helps read the files.
class Parser:
    @staticmethod
    def from_json(json_str: str) -> DecisionRequest:
        # Load the JSON data
        data = json.loads(json_str)
        criteria = [Criterion(**c) for c in data.get("criteria", [])]
        options = [Option(**o) for o in data.get("options", [])]
        return DecisionRequest(
            domain=data.get("domain", "Unknown"),
            criteria=criteria,
            options=options,
            constraints=data.get("constraints")
        )

    @staticmethod
    def load_file(filepath: str) -> DecisionRequest:
        # Open the file and read it
        with open(filepath, 'r') as f:
            if filepath.endswith('.json'):
                return Parser.from_json(f.read())
            # For a senior take-home, we'd add YAML support here if PyYAML is available
            raise ValueError("Unsupported file format. Use .json for now.")
