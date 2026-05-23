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
- [x] **High-Level Requirements (HLR)**:
  - [x] Initialize `verification/reqs/hlr.yaml` with schema and metadata.
  - [x] Extract and formalize pilot HLRs (Functional, Output, Resource).
  - [x] Complete HLR extraction for *The TeXbook*.
  - [x] Complete HLR extraction for *The Metafontbook*.
- [x] **Low-Level Requirements (LLR)**:
  - [x] Initialize `verification/reqs/llr_tex.yaml` and `verification/reqs/llr_mf.yaml`.
  - [x] Map pilot WEB sections to LLRs (Introduction, Char Set, I/O, Strings).
  - [x] Complete LLR mapping for TeX (`tex.web`):
    - [x] Parts 1-4 (Introduction, Character set, I/O, Strings).
    - [x] Parts 5-6 (Printing, Error reporting).
    - [x] Parts 7-10 (Arithmetic, Packed data, Dynamic memory, Box data structures).
    - [x] Parts 11-20 (Memory layout, Displaying/Destroying/Copying boxes, Command codes, Semantic nest, Equivalents, Hash table, Saving/Restoring, Token lists).
    - [x] Parts 21-30 (Syntactic routines, Input stacks, Next token, Expansion, Scanning, Building token lists, Conditionals, File names, Font metric data).
    - [x] Parts 31-40 (DVI format, Shipping pages out, Packaging, Math mode data structures/subroutines/formulas, Alignment, Breaking paragraphs, Pre-hyphenation).
    - [x] Parts 41-43 (Post-hyphenation, Hyphenation, Initializing hyphenation tables).
    - [x] Parts 44-46 (Breaking vertical lists into pages, Page builder, Chief executive).
    - [x] Parts 47-49 (Building boxes and lists, Building math lists, Mode-independent processing).
    - [x] Parts 50-55 (Dumping, Main program, Debugging, Extensions, System-dependent).
  - [x] Complete LLR mapping for Metafont (`mf.web`):
    - [x] Parts 1-5 (Introduction, Character set, I/O, Strings, Printing).
    - [x] Parts 6-10 (Error reporting, Arithmetic, Algebraic functions, Packed data, Dynamic memory).
    - [x] Parts 11-20 (Memory layout, Command codes, Hash table, Token lists, Variables, Saving/Restoring, Paths, Control points, Discrete moves, Edge structures).
    - [x] Parts 21-30 (Octants, Filling contour, Polygonal pens, Filling envelope, Elliptical pens, Direction/Intersection, Online graphic, Linear/Nonlinear equations, Syntactic routines).
    - [x] Parts 31-40 (Input stacks, Next token, Macro definitions, Expansion, Conditionals, Iterations, File names, Parsing routines/expressions).
    - [x] Parts 41-42 (Parsing expressions, Doing the operations).
    - [x] Parts 43-45 (Statements and commands, Commands, Font metric data).
    - [x] Parts 46-48 (GF format, Shipping characters out, Dumping).
    - [x] Parts 49-52 (Main program, Debugging, System-dependent).
- [x] **Traceability Matrix**:
  - [x] Initialize `verification/trace/matrix.yaml` with bi-directional schema.
  - [x] Establish HLR-to-LLR traces for pilot requirements.
  - [x] Ensure all HLRs trace to LLRs and vice versa for the full set.

## Phase 3: Test Harness & Automation Development
- [x] **Harness Core Architecture**:
  - [x] Create `verification/harness/runner.py` skeleton with CLI (argparse).
  - [x] Implement configuration loading (YAML).
  - [x] Implement logging and result reporting infrastructure.
- [x] **Automated Workflow Modules**:
  - [x] Implement `Tangle` wrapper (WEB to Pascal).
  - [x] Implement `Compile` wrapper (Pascal to executable).
  - [x] Implement `Execute` wrapper with environment isolation.
  - [x] Implement `Normalize` utility for text-based outputs (Log, Terminal).
  - [x] Implement `Compare` module for automated pass/fail determination:
    - [x] Implement core comparison logic and reporting.
    - [x] Implement floating-point tolerance handling for numerical outputs.
    - [x] Implement delegation to symbolic comparators for binary formats.
- [x] **Symbolic Comparators**:
  - [x] Develop DVI comparator (using `DVItype`).
  - [x] Develop GF/PK comparators (using `GFtype` and `PKtype`).
  - [x] Develop TFM comparator (using `TFtoPL`).

## Phase 4: Requirements-Based Testing (RBT) Implementation
- [ ] **Baseline Integration**:
  - [x] Automate the TRIP (TeX) torture test:
    - [x] Create `TRIP` test configuration and directory.
    - [x] Automate `TANGLE` on `tex.web` with `trip.ch`.
    - [x] Automate compilation of `trip.p`.
    - [x] Automate `INITEX` run to generate `trip.fmt`.
    - [x] Automate `TRIP` execution and comparison of `.log`, `.typ`, and `.tfm` files.
  - [x] Automate the TRAP (Metafont) torture test:
    - [x] Create `TRAP` test configuration and directory.
    - [x] Automate `TANGLE` on `mf.web` with `trap.ch`.
    - [x] Automate compilation of `trap.p`.
    - [x] Automate `INIMF` run to generate `trap.base`.
    - [x] Automate `TRAP` execution and comparison of `.log`, `.typ`, and `.tfm` files.
- [ ] **Normal Range Testing**:
  - [ ] Develop test cases for standard compilation and font generation:
    - [ ] Implement `STORY` test case (Basic TeX paragraph breaking).
    - [x] Implement `HELLO` test case (Basic TeX macro expansion).
    - [ ] Implement `LOGO` test case (Metafont character generation).
- [ ] **Robustness Testing**:
  - [ ] Implement Boundary Value Analysis (BVA) tests:
    - [ ] Develop BVA tests for TeX integer registers (max/min values).
    - [ ] Develop BVA tests for Metafont coordinate ranges.
  - [ ] Implement Error Handling and Resource Exhaustion tests:
    - [ ] Develop tests for TeX stack overflow (macro recursion).
    - [ ] Develop tests for Metafont memory exhaustion (complex paths).
    - [ ] Develop tests for file-not-found and invalid input syntax.
- [x] **Traceability**:
  - [x] Map all test cases to HLRs and LLRs in the traceability matrix.

## Phase 5: Structural Coverage & MC/DC Analysis
- [ ] **Instrumentation**:
  - [ ] Develop the Pascal parser/instrumenter for `TANGLE` output:
    - [x] Implement Lexer for Pascal subset:
      - [x] Define Pascal tokens and regular expressions for TANGLE subset.
      - [x] Implement token scanning and error handling.
      - [x] Develop unit tests for the Lexer with sample TANGLE output.
    - [ ] Implement basic Pascal statement parsing and probe insertion:
      - [x] Implement parser for Pascal assignment and procedure call statements.
      - [x] Implement parser for compound statements (BEGIN...END).
      - [x] Implement parser for conditional statements (IF...THEN...ELSE).
      - [x] Implement parser for iterative statements (WHILE, REPEAT, FOR).
      - [ ] Develop logic for inserting unique probe IDs before each decision point.
      - [ ] Verify probe insertion on simple Pascal programs.
    - [x] Implement robust boolean expression parsing.
    - [ ] Implement decision and condition identification logic.
  - [ ] Implement the `record_mcdc` runtime library:
    - [ ] Develop the runtime library for bit-mask recording:
      - [ ] Define data structures for efficient bit-mask storage.
      - [ ] Implement thread-safe (if necessary) recording functions.
    - [ ] Implement coverage data persistence and export:
      - [ ] Develop routines to write coverage data to disk upon program termination.
      - [ ] Implement a post-processor to convert raw masks to a human-readable format.
- [ ] **Execution & Analysis**:
  - [ ] Run RBT suite with instrumentation enabled.
  - [ ] Perform MC/DC analysis on collected data.
- [ ] **Gap Analysis & Augmentation**:
  - [ ] Identify uncovered code.
  - [ ] Create augmented test cases to achieve 100% MC/DC.
  - [ ] Document justifications for any unavoidable gaps (VAR).

## Phase 6: Tool Qualification & Final Certification
- [ ] **Tool Qualification**:
  - [ ] Perform qualification for the Test Harness and Comparators:
    - [ ] Define Tool Operational Requirements (TOR).
    - [ ] Develop Qualification Test Suite (QTS) for Harness.
    - [ ] Execute QTS and generate Tool Qualification Report (TQR).
  - [ ] Perform qualification for the MC/DC Instrumenter:
    - [ ] Define TOR for Instrumenter.
    - [ ] Develop QTS for Instrumenter (MC/DC validation).
    - [ ] Execute QTS and generate TQR for Instrumenter.
  - [ ] Verify `TANGLE` and the Pascal compiler or their outputs.
- [ ] **Final Documentation**:
  - [ ] Generate the final Traceability Report.
  - [ ] Generate the Verification Results Report.
  - [ ] Finalize the Verification Analysis Report (VAR).
