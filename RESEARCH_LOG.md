# Research Log & Architectural Decision Records (ADR)

## ADR 01: Multi-Criteria Decision Model
**Decision**: Chose **Simple Additive Weighting (SAW)**.
**Reasoning**: While AHP (Analytic Hierarchy Process) is more rigorous, SAW is significantly more explainable to non-technical stakeholders (CTOs/Product Managers). It allows for a "receipt-style" breakdown of scores.

## ADR 02: Language & Portability
**Decision**: Python with standard `dataclasses`.
**Reasoning**: Initially planned Pydantic for validation, but stripped it to zero-dependency `dataclasses` to ensure the project runs on any environment without `pip install`.

## ADR 03: Normalization Technique
**Decision**: **Min-Max Scaling**.
**Reasoning**: Provides the most intuitive 0-1 range. Identified a weakness with outliers (e.g. one very expensive option skewing results) and documented it in the Critical Review section of the implementation plan.

## Ambiguities Resolved
- **Hard Constraints**: Decided to disqualify options that fail "Must-Haves" before scoring starts.
- **Missing Data**: Currently handles missing data by flagging options as "Ineligible" to prevent misleading scores.
