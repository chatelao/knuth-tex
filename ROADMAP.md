# Verification Roadmap for TeX and Metafont (DO-178B Level A)

This roadmap outlines the steps required to achieve DO-178B Level A certification for the TeX and Metafont systems, as derived from the Test Concept and Test Design documents.

## Phase 1: Verification Infrastructure Setup
- [x] Establish the `verification/` directory structure:
  - `verification/reqs/`
  - `verification/tests/`
  - `verification/trace/`
  - `verification/harness/`
  - `verification/results/`
- [x] Initialize repository-level configurations for the verification environment.

## Phase 2: Requirements Definition & Traceability
- [ ] **High-Level Requirements (HLR)**:
  - [x] Initialize `verification/reqs/hlr.yaml` with schema and metadata.
  - [x] Extract and formalize pilot HLRs (Functional, Output, Resource).
  - [ ] Complete HLR extraction for *The TeXbook*.
  - [ ] Complete HLR extraction for *The Metafontbook*.
- [ ] **Low-Level Requirements (LLR)**:
  - [x] Initialize `verification/reqs/llr_tex.yaml` and `verification/reqs/llr_mf.yaml`.
  - [x] Map pilot WEB sections to LLRs (Introduction, Char Set, I/O, Strings).
  - [ ] Complete LLR mapping for TeX (`tex.web`):
    - [x] Parts 1-4 (Introduction, Character set, I/O, Strings).
    - [x] Parts 5-6 (Printing, Error reporting).
    - [x] Parts 7-10 (Arithmetic, Packed data, Dynamic memory, Box data structures).
    - [x] Parts 11-20 (Memory layout, Displaying/Destroying/Copying boxes, Command codes, Semantic nest, Equivalents, Hash table, Saving/Restoring, Token lists).
    - [x] Parts 21-30 (Syntactic routines, Input stacks, Next token, Expansion, Scanning, Building token lists, Conditionals, File names, Font metric data).
    - [x] Parts 31-40 (DVI format, Shipping pages out, Packaging, Math mode data structures/subroutines/formulas, Alignment, Breaking paragraphs, Pre-hyphenation).
    - [ ] Parts 41-55 (Hyphenation, Breaking vertical lists into pages, Page builder, Chief executive, Building boxes/math lists, Mode-independent processing, Dumping, Main program, Debugging, Extensions, System-dependent).
  - [ ] Complete LLR mapping for Metafont (`mf.web`):
    - [x] Parts 1-5 (Introduction, Character set, I/O, Strings, Printing).
    - [x] Parts 6-10 (Error reporting, Arithmetic, Algebraic functions, Packed data, Dynamic memory).
    - [x] Parts 11-20 (Memory layout, Command codes, Hash table, Token lists, Variables, Saving/Restoring, Paths, Control points, Discrete moves, Edge structures).
    - [x] Parts 21-30 (Octants, Filling contour, Polygonal pens, Filling envelope, Elliptical pens, Direction/Intersection, Online graphic, Linear/Nonlinear equations, Syntactic routines).
    - [ ] Parts 31-40 (Input stacks, Next token, Macro definitions, Expansion, Conditionals, Iterations, File names, Parsing routines/expressions).
    - [ ] Parts 41-52 (Parsing continued, Statements, Commands, Font metric data, Shipping out, GF format, Online display, CM fonts, Initializing, Dumping, Main program, Debugging, System-dependent).
- [ ] **Traceability Matrix**:
  - [x] Initialize `verification/trace/matrix.yaml` with bi-directional schema.
  - [x] Establish HLR-to-LLR traces for pilot requirements.
  - [ ] Ensure all HLRs trace to LLRs and vice versa for the full set.

## Phase 3: Test Harness & Automation Development
- [ ] **Harness Core Architecture**:
  - [x] Create `verification/harness/runner.py` skeleton with CLI (argparse).
  - [x] Implement configuration loading (YAML).
  - [x] Implement logging and result reporting infrastructure.
- [ ] **Automated Workflow Modules**:
  - [x] Implement `Tangle` wrapper (WEB to Pascal).
  - [x] Implement `Compile` wrapper (Pascal to executable).
  - [x] Implement `Execute` wrapper with environment isolation.
  - [x] Implement `Normalize` utility for text-based outputs (Log, Terminal).
  - [ ] Implement `Compare` module for automated pass/fail determination:
    - [x] Implement core comparison logic and reporting.
    - [ ] Implement floating-point tolerance handling for numerical outputs.
    - [ ] Implement delegation to symbolic comparators for binary formats.
- [ ] **Symbolic Comparators**:
  - [ ] Develop DVI comparator (using `DVItype`).
  - [ ] Develop GF/PK comparator (using `GFtype`).
  - [ ] Develop TFM comparator (using `TFtoPL`).

## Phase 4: Requirements-Based Testing (RBT) Implementation
- [ ] **Baseline Integration**:
  - [ ] Automate the TRIP (TeX) torture test:
    - [ ] Create `TRIP` test configuration and directory.
    - [ ] Automate `TANGLE` on `tex.web` with `trip.ch`.
    - [ ] Automate compilation of `trip.p`.
    - [ ] Automate `INITEX` run to generate `trip.fmt`.
    - [ ] Automate `TRIP` execution and comparison of `.log`, `.typ`, and `.tfm` files.
  - [ ] Automate the TRAP (Metafont) torture test:
    - [ ] Create `TRAP` test configuration and directory.
    - [ ] Automate `TANGLE` on `mf.web` with `trap.ch`.
    - [ ] Automate compilation of `trap.p`.
    - [ ] Automate `INIMF` run to generate `trap.base`.
    - [ ] Automate `TRAP` execution and comparison of `.log`, `.typ`, and `.tfm` files.
- [ ] **Normal Range Testing**:
  - [ ] Develop test cases for standard compilation and font generation.
- [ ] **Robustness Testing**:
  - [ ] Implement Boundary Value Analysis (BVA) tests.
  - [ ] Implement Error Handling and Resource Exhaustion tests.
- [ ] **Traceability**:
  - [ ] Map all test cases to HLRs and LLRs in the traceability matrix.

## Phase 5: Structural Coverage & MC/DC Analysis
- [ ] **Instrumentation**:
  - [ ] Develop the Pascal parser/instrumenter for `TANGLE` output:
    - [ ] Implement basic Pascal statement parsing and probe insertion.
    - [ ] Implement robust boolean expression parsing.
    - [ ] Implement decision and condition identification logic.
  - [ ] Implement the `record_mcdc` runtime library:
    - [ ] Develop the runtime library for bit-mask recording.
    - [ ] Implement coverage data persistence and export.
- [ ] **Execution & Analysis**:
  - [ ] Run RBT suite with instrumentation enabled.
  - [ ] Perform MC/DC analysis on collected data.
- [ ] **Gap Analysis & Augmentation**:
  - [ ] Identify uncovered code.
  - [ ] Create augmented test cases to achieve 100% MC/DC.
  - [ ] Document justifications for any unavoidable gaps (VAR).

## Phase 6: Tool Qualification & Final Certification
- [ ] **Tool Qualification**:
  - [ ] Perform qualification for the Test Harness and Comparators.
  - [ ] Perform qualification for the MC/DC Instrumenter.
  - [ ] Verify `TANGLE` and the Pascal compiler or their outputs.
- [ ] **Final Documentation**:
  - [ ] Generate the final Traceability Report.
  - [ ] Generate the Verification Results Report.
  - [ ] Finalize the Verification Analysis Report (VAR).
