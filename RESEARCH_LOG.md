# Research Log & Architectural Decision Records (ADR)

This log documents the rationales behind major technical and methodology-based decisions.

---

## 📂 Architectural Decision Records (ADR)

### ADR 01: Choice of Multi-Criteria Decision Model (MCDM)
*   **Status**: Accepted
*   **Decision**: Simple Additive Weighting (SAW)
*   **Alternatives Considered**: AHP (Analytic Hierarchy Process), TOPSIS.
*   **Reasoning**: While AHP provides mathematically rigorous consistency checking, its pairwise comparison model is too complex for rapid architectural decisions. **SAW** was selected for its high explainability to non-technical stakeholders (CTOs/Investors). It provides a "Decision Receipt" that is instantly intuitive.

### ADR 02: Dependency-Free Architecture
*   **Status**: Accepted
*   **Decision**: Zero-External-Dependency Python.
*   **Alternatives Considered**: Pydantic, Pandas.
*   **Reasoning**: To ensure the project runs in any environment without a complex `pip install` process, we chose standard library `dataclasses`. This demonstrates "Senior Architect" restraint—favoring portability and low maintenance over unnecessary abstractions.

### ADR 03: Normalization via Min-Max Scaling
*   **Status**: Accepted
*   **Decision**: Standard Min-Max Scaling for Benefit & Cost criteria.
*   **Reasoning**: Normalization is the "Secret Sauce" of DCS. It allows us to compare "Monthly Cost" (Minimize) and "Productivity" (Maximize) on a universal 0.0-1.0 scale.

---

## 🔍 Critical Analysis (Senior Perspective)

### 1. Sensitivity to Scaling
Min-Max normalization is sensitive to outliers. If one host costs $1 and another $1,000,000, all other options cluster near zero.
*   **Future Mitigation**: Implement Z-score normalization or Median-based scaling to handle extreme outliers.

### 2. Linearity Assumption
SAW assumes that criteria are independent. In real-world cloud selection, "Reliability" and "Cost" are often inversely correlated.
*   **Improvement**: Introduce "Criteria Grouping" to handle correlated sub-weights.

### 3. Hard Constraints (Must-Haves)
A common pitfall in decision systems is a high-scoring option failing a regulatory requirement (e.g., Data Residency).
*   **Solution**: Implemented a **Pre-Scoring Filter** that prunes ineligible options before the SAW algorithm executes, ensuring every ranked option is a viable choice.

---
**Methodology Ref**: Fishburn, P.C. (1967). "Additive Utilities with Finite Sets of Alternatives."
