# DO-178B Level A Test Design for TeX and Metafont

## 1. Introduction
This document defines the detailed test design, tooling, and structures required to implement the verification strategy outlined in `DO178B_TEST_CONCEPT.md`. It provides the technical specifications for requirements traceability, test execution automation, and structural coverage analysis necessary for DO-178B Level A compliance.

## 2. Requirements and Traceability Structure
To ensure bi-directional traceability and machine-readability, requirements and traceability data will be stored in YAML format.

### 2.1 Requirements Schema

#### 2.1.1 High-Level Requirements (HLR)
HLRs are stored in `verification/reqs/hlr.yaml`.
```yaml
- id: HLR-TEX-FUN-001
  description: "The TeX system shall implement the line breaking algorithm as specified in The TeXbook, Part 14."
  category: Functional
  source: "The TeXbook, p. 94"
```

#### 2.1.2 Low-Level Requirements (LLR)
LLRs are stored in `verification/reqs/llr_tex.yaml` and `verification/reqs/llr_mf.yaml`. Each LLR corresponds to one or more WEB sections.
```yaml
- id: LLR-TEX-SEC-813
  web_section: 813
  description: "The second pass of the line-breaking algorithm shall be entered if the first pass did not find a feasible solution with threshold 'pretolerance'."
  parent_hlr:
    - HLR-TEX-FUN-001
```

### 2.2 Traceability Matrix Schema
The traceability matrix is maintained in `verification/trace/matrix.yaml`, linking HLRs, LLRs, and Test Cases.
```yaml
- hlr_id: HLR-TEX-FUN-001
  llr_ids:
    - LLR-TEX-SEC-813
    - LLR-TEX-SEC-814
  test_case_ids:
    - TC-TEX-LINE-001
    - TC-TEX-LINE-002
```

### 2.3 Directory Structure
The verification environment shall follow this layout:
- `verification/`
  - `reqs/`: YAML files for HLRs and LLRs.
  - `tests/`: Test scripts, input files (.tex, .mf), and expected outputs.
  - `trace/`: Traceability matrix and coverage mapping.
  - `harness/`: Python scripts for test automation.
  - `results/`: Execution logs, generated artifacts, and coverage reports.

## 3. Test Execution and Harness
Test execution is automated via a Python-based test harness located in `verification/harness/runner.py`.

### 3.1 Automated Workflow
For each test case, the harness performs the following steps:
1.  **Tangle**: Run `TANGLE` on the `.web` source and associated `.ch` change file to generate Pascal code.
2.  **Instrument (Optional)**: If running coverage, instrument the Pascal code (see Section 4).
3.  **Compile**: Compile the Pascal code using the target compiler (e.g., a Pascal-to-C translator or a native Pascal compiler).
4.  **Execute**: Run the executable with the specified test input (`.tex` or `.mf`).
5.  **Compare**:
    -   Log files (`.log`) are compared using a normalized `diff` (ignoring dates/paths).
    -   Binary outputs (`.dvi`, `.gf`, `.tfm`) are converted to symbolic formats using `DVItype`, `GFtype`, `TFtoPL`, and `PLtoTF` before comparison.
    -   Terminal output (`.fot`) is compared against recorded baselines.

### 3.2 Result Categorization
-   **Pass**: All outputs match the expected baselines exactly (within rounding tolerances defined in TRIP/TRAP).
-   **Fail**: Mismatch in output, crash, or timeout.
-   **Inconclusive**: Harness failure or missing baseline data.

## 4. MC/DC Instrumentation and Coverage Strategy
For Level A compliance, 100% MC/DC is required. Since standard coverage tools for Pascal may not be available in all target environments, a custom instrumentation strategy is employed.

### 4.1 Instrumentation Approach
The test harness includes a Pascal parser/instrumenter that processes the output of `TANGLE`.
1.  **Boolean Expression Analysis**: The tool identifies all complex boolean expressions in `if`, `while`, and `until` statements.
2.  **Probe Insertion**: For each condition $c$ in a decision $d$, a probe is inserted to record the value of $c$ and the resulting $d$.
    -   *Original*: `if (a > 0) and (b < 10) then`
    -   *Instrumented*: `if record_mcdc(probe_id, (a > 0), (b < 10)) then`
3.  **Runtime Collection**: The `record_mcdc` function (provided in a library) updates a bit-mask representing the truth table of conditions seen during execution.

### 4.2 Coverage Analysis
-   **MC/DC Verification**: Post-execution, a tool analyzes the collected truth tables to determine if each condition has been shown to independently affect the decision's outcome.
-   **Coupled Conditions**: Any coupled conditions that cannot be shown to be independent must be documented and justified in a Verification Analysis Report (VAR).

## 5. Integration of TRIP/TRAP Tests
The existing TRIP (TeX) and TRAP (Metafont) torture tests are integrated into the RBT suite as a "Robustness and Regression" baseline.

### 5.1 TRIP/TRAP Automation
The test harness reproduces the manual steps defined in `tripman.tex` and `trapman.tex` automatically:
1.  Initialize with `INITEX` / `INIMF`.
2.  Generate `.fmt` / `.base` (e.g., `trip.fmt`).
3.  Run the test file (`trip.tex` / `trap.mf`).
4.  Perform the multi-stage comparison against master appendices (Log, DVI/GF, TFM, and Terminal output).

### 5.2 Augmentation Strategy
Since TRIP/TRAP were designed for statement coverage, they will be augmented with new test cases (`TC-TEX-*`, `TC-MF-*`) specifically targeting:
-   Uncovered LLRs (WEB sections) identified during coverage analysis.
-   Boundary conditions for every LLR.
-   Specific MC/DC condition pairs not exercised by the torture tests.

## 6. Tool Qualification
All tools used in the verification path must be qualified or their output manually verified according to DO-178B Section 12.2.

-   **Test Harness & Comparators**: Qualified as Verification Tools.
-   **MC/DC Instrumenter**: Qualified as a Verification Tool.
-   **TANGLE & Compiler**: The output of the compiler (object code) must be verified against the source code unless the compiler itself is qualified as a Development Tool.
