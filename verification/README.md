# Verification Artifacts for TeX and Metafont (DO-178B Level A)

This directory contains all artifacts related to the DO-178B Level A verification of the TeX and Metafont systems.

## Directory Structure

- `reqs/`: Contains High-Level Requirements (HLR) and Low-Level Requirements (LLR) formalized in YAML.
- `tests/`: Contains test scripts, input files (`.tex`, `.mf`), and expected output baselines.
- `trace/`: Contains the bi-directional traceability matrix and coverage mapping data.
- `harness/`: Contains the Python-based test harness and automation scripts.
- `results/`: Contains execution logs, generated artifacts, and structural coverage reports.

## Reference Documents

- `DO178B_TEST_CONCEPT.md`: High-level verification strategy.
- `DO178B_TEST_DESIGN.md`: Detailed technical specification for the verification environment.
- `ROADMAP.md`: Project status and planned verification milestones.
