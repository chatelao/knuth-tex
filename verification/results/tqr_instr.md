# Tool Qualification Report for the MC/DC Instrumenter (TQR-INSTR)

| Requirement ID | Description | Test Files | Status |
| --- | --- | --- | --- |
| TOR-INSTR-001 | The instrumenter shall support a subset of the Pascal grammar sufficient for parsing TANGLE output, including PROGRAM, LABEL, CONST, TYPE, VAR, PROCEDURE, and FUNCTION declarations. | test_parser.py | PASSED |
| TOR-INSTR-002 | The instrumenter shall identify all decision points in the code, including IF, WHILE, REPEAT-UNTIL, FOR, and CASE statements. | test_instrumenter.py, test_parser.py | PASSED |
| TOR-INSTR-003 | The instrumenter shall decompose complex boolean expressions within decision points into atomic conditions. | test_instrumenter.py | PASSED |
| TOR-INSTR-004 | The instrumenter shall assign a unique ID to each identified decision point within a program. | test_instrumenter.py | PASSED |
| TOR-INSTR-005 | The instrumenter shall assign a unique ID to each atomic condition within a decision point. | test_instrumenter.py | PASSED |
| TOR-INSTR-006 | The instrumenter shall inject 'mcdc_begin' probe calls at the start of each decision point. | test_instrumenter.py | PASSED |
| TOR-INSTR-007 | The instrumenter shall wrap atomic conditions with 'mcdc_cond' probe calls to record their evaluation during runtime. | test_instrumenter.py | PASSED |
| TOR-INSTR-008 | The instrumenter shall provide a mechanism to selectively instrument only specified routines (procedures or functions). | test_instrumenter.py | PASSED |
| TOR-INSTR-009 | The instrumenter shall perform a Pascal-to-Pascal transformation, emitting valid Pascal source code from the instrumented Abstract Syntax Tree (AST). | test_instrumenter.py, test_integration.py | PASSED |
| TOR-INSTR-010 | The instrumenter shall support the 'otherwise' clause in CASE statements. | test_parser.py, test_instrumenter.py | PASSED |
| TOR-INSTR-011 | The instrumenter shall correctly handle labels and GOTO statements in the Pascal source. | test_parser.py, test_instrumenter.py | PASSED |
| TOR-INSTR-012 | The instrumenter shall prepend a runtime inclusion directive (e.g., #include 'runtime.p') to the generated instrumented source file. | test_integration.py | PASSED |
