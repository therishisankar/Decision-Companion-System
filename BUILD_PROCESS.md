# Build & Development Process

The Decision Companion System (DCS) is architected for maximum portability and zero-dependency execution. This document details the engineering process and technical stack.

## Technical Requirements
- **Runtime**: Python 3.10+ (Standard Library only)
- **Dependencies**: 0 External dependencies (Zero-bloat architecture).
- **Interface**: Stateless Command Line Interface (CLI).

## Architecture: Modular Pipeline
The system follows a pure functional pipeline to ensure 100% auditability of decision logic:

1. **Ingestion**: Validates JSON/YAML structure and ensures schema compliance.
2. **Filtering**: Executes a "Hard Constraint" pass to prune ineligible options (e.g., Budget/Compliance).
3. **Normalization**: Maps diverse units ($, %, ms) to a uniform 0.0 - 1.0 interval.
4. **Weighted Scoring**: Applies Simple Additive Weighting (SAW) to produce the final recommendation.
5. **Enrichment**: Generates the "Explainability Trace" and Sensitivity Analysis.

## Project Structure
```text
DCS/
├── src/
│   ├── core/           # Math & Logic (Normalizer, Scorer)
│   ├── explain/        # Explainability & Sensitivity Logic
│   ├── io/             # Data Parsing & Reporting
│   └── models/         # Type-safe Data Contracts
├── templates/          # Standard decision configurations
└── tests/              # Automated verification suite
```

## Running the System
The system is designed as a portable Python package.

### Standard Execution:
```powershell
$env:PYTHONPATH = "."; python src/cli.py templates/cloud_decision.json
```

### Verification (Tests):
The core logic is verified using standard Python `unittest`.
```powershell
python -m unittest discover tests
```

## Engineering Philosophy
- **Statelessness**: Every decision run is independent and audit-logged in stdout.
- **Fail-Fast**: Invalid inputs or constraint violations trigger explicit errors rather than "guessed" averages.
- **Explainability First**: Code is not just about results; it's about $proving$ them. Every calculation is exposed via the `Presenter` layer.
