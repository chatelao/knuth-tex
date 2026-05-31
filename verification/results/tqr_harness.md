# Tool Qualification Report for the Test Harness (TQR-HARNESS)

| Requirement ID | Description | Test Files | Status |
| --- | --- | --- | --- |
| TOR-HARNESS-001 | The harness shall provide a Tangle wrapper to convert WEB source files and optional change files into Pascal source and string pool files using the TANGLE processor. | test_tangle.py | PASSED |
| TOR-HARNESS-002 | The harness shall provide a Compile wrapper to invoke a Pascal compiler for generating executable binaries from Pascal source files. | test_compiler.py | PASSED |
| TOR-HARNESS-003 | The harness shall provide an Execute wrapper to run the generated binaries with specified command-line arguments and standard input. | test_executor.py | PASSED |
| TOR-HARNESS-004 | The harness shall implement environment isolation for test execution by running binaries in dedicated subdirectories. | test_executor.py | PASSED |
| TOR-HARNESS-005 | The harness shall provide a Comparison module to perform automated pass/fail determination by comparing actual output files with expected baselines. | test_comparer.py | PASSED |
| TOR-HARNESS-006 | The Comparison module shall support text-based comparison with configurable normalization (e.g., whitespace collapsing). | test_comparer.py | PASSED |
| TOR-HARNESS-007 | The Comparison module shall support symbolic comparison for binary formats (DVI, GF, PK, TFM) by delegating to specialized converters (DVItype, GFtype, PKtype, TFtoPL). | test_symbolic_comparators.py | PASSED |
| TOR-HARNESS-008 | The harness shall support multi-stage test execution as defined in test configuration files. | test_runner.py | PASSED |
| TOR-HARNESS-009 | The harness shall capture and log terminal output (stdout and stderr) for each test execution. | test_runner.py | PASSED |
| TOR-HARNESS-010 | The harness shall provide a mechanism to load global and test-specific configurations from YAML files. | test_runner.py | PASSED |
