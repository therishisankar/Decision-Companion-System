# AI Usage Transparency Report

This document outlines the role of Artificial Intelligence (AI) in the development of the Decision Companion System (DCS).

## Intent
The goal of using AI in this project was to act as an "Architect's Assistant" to accelerate research, boilerplate generation, and documentation drafting, while maintaining human clinical oversight of the core decision logic.

## Specific AI Contributions
1.  **Design Brainstorming**: AI helped identify the "Cloud Infrastructure Selection" domain as a strong candidate for demonstrating multi-criteria logic.
2.  **Documentation Drafting**: Initial drafts for the `README.md` and `implementation_plan.md` were generated with AI assistance.
3.  **Data Templates**: The `cloud_decision.json` sample was generated to provide realistic dummy data for testing.

## Human Oversight & Control
The follow elements were **fully architected and verified by the Human Lead**:
-   Mathematical Choice: The decision to use **SAW (Simple Additive Weighting)** over AHP.
-   Core Scorer Logic: The implementation of normalization and weighted sums (src/core).
-   System Architecture: The modular pipeline design ensuring decoupling of IO from Math.

## Conclusion
The DCS stands as a product of "Human-Centric AI Development," where AI empowered the architect to focus on high-level design while automating routine implementation tasks.
