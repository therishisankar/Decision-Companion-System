# Decision Companion System (DCS)

An explainable decision engine developed as an architectural take-home assignment.

## Objective
The DCS demonstrates how to decompose complex, subjective decisions (like Cloud Infrastructure selection) into a transparent, weighted mathematical model.

## Core Features
1.  **Weighted Scoring (SAW)**: Multi-criteria decision making with user-defined weights.
2.  **Normalization Engine**: Compares "Apples to Oranges" by scaling diverse metrics (Cost, Uptime, Expertise) to a 0.0-1.0 range.
3.  **Explainability Layer**: Every score comes with a full mathematical breakdown.
4.  **Sensitivity Analysis**: Identifies how stable a decision is.

## Project Structure
- `src/core/`: The "Brain". Pure math logic (Normalizer, Scorer).
- `src/models/`: Data schemas using Python `dataclasses`.
- `src/io/`: Parsers for JSON inputs and CLI presenters.
- `src/explain/`: Analysis tools for "What-if" scenarios.

## Quick Start
1.  Navigate to `e:\DCS`.
2.  Run the CLI with a sample template:
    ```bash
    python src/cli.py templates/cloud_decision.json
    ```

## Responsible AI Usage
AI is used for:
- Drafting criteria templates.
- Summarizing the logic for stakeholders.
AI is **excluded** from the scoring math to ensure 100% auditability.
