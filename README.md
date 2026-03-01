# Decision Companion System (DCS)

**Architectural Decision Engine for High-Stakes Selection**

---

## 🎯 Overview

The **Decision Companion System (DCS)** is a professional-grade, explainable decision-making engine. It provides a formal framework to decompose complex, subjective architectural choices into an auditable, weighted mathematical model.

Designed with **Senior Architectural Rigor**, DCS removes the "Black Box" of decision-making by providing a transparent "Math Receipt" for every recommendation.

## 🏗️ Core Architecture: The "DCS Pipeline"

DCS is built as a pure functional pipeline to ensure deterministic results and zero side-effects during scoring.

```mermaid
graph LR
    A[JSON/YAML Input] --> B[Validator]
    B --> C[Constraint Filter]
    C --> D[Normalization Engine]
    D --> E[Weighted Scorer (SAW)]
    E --> F[Explainability Trace]
    F --> G[CLI Report & Analysis]
```

## ✨ Professional Features

*   **Weighted Criteria (SAW)**: Implements the Simple Additive Weighting (SAW) model for multi-criteria decision making (MCDM).
*   **Normalization Engine**: Automates "Apples-to-Oranges" comparisons by scaling cost (Minimize) and performance (Maximize) metrics to a uniform 0.0-1.0 interval.
*   **Explainability Layer**: Generates a detailed breakdown of every calculation (Value -> Normalized -> Weighted Score).
*   **Hard Constraint Enforcement**: A safety "Kill Switch" that prunes options failing mandatory requirements (e.g., Budget, Compliance).
*   **Sensitivity Analysis**: Mathematically identifies the "Decision Stability" (the score gap between the winner and runner-up).

## 🚀 Quick Start

Ensure you have **Python 3.10+** installed. No external dependencies are required.

```bash
# Run the core demonstration (Cloud Infrastructure Selection)
python src/cli.py templates/cloud_decision.json

# Run the budget violation demo (Hard Constraint Check)
python src/cli.py templates/budget_violation.json
```

## 📂 Project Documentation

*   [BUILD_PROCESS.md](./BUILD_PROCESS.md): Technical stack, structure, and engineering philosophy.
*   [RESEARCH_LOG.md](./RESEARCH_LOG.md): Architectural Decision Records (ADR) and MCDM theory.
*   [AI_USAGE.md](./AI_USAGE.md): Transparency report on the collaborative role of AI in this project.

---
**Author**: [Your Name/GitHub Handle]  
**Architecture**: Senior-Level Modular Decision Engine
