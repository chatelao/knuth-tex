import pytest
import os
from pathlib import Path
from verification.harness.verify_pascal_extensions import PascalExtensionValidator

def test_validator_declaration_header(tmp_path):
    header = tmp_path / "test.h"
    header.write_text("argc:asmname '_p_argc' Integer;\nprocedure argv(no:Integer;var str:string); external;")

    pascal = tmp_path / "test.p"
    pascal.write_text('#include "test.h"\nbegin for a:=1 to argc-1 do argv(a,s); end.')

    validator = PascalExtensionValidator(pascal, header)
    assert validator.check_declaration("argc") is True
    assert validator.check_declaration("argv") is True
    assert validator.check_declaration("exit") is False

def test_validator_declaration_pascal(tmp_path):
    pascal = tmp_path / "test.p"
    pascal.write_text("procedure exit(x:integer); external;\nbegin exit(0); end.")

    validator = PascalExtensionValidator(pascal)
    assert validator.check_declaration("exit") is True

def test_validator_usage(tmp_path):
    pascal = tmp_path / "test.p"
    pascal.write_text("begin for a:=1 to argc-1 do argv(a,s); flushstdout; end.")

    validator = PascalExtensionValidator(pascal)
    assert validator.check_usage("argc") is True
    assert validator.check_usage("argv") is True
    assert validator.check_usage("flushstdout") is True
    assert validator.check_usage("nonexistent") is False

def test_validator_auto_header_discovery(tmp_path):
    header = tmp_path / "tangext.h"
    header.write_text("argc:asmname '_p_argc' Integer;")

    pascal = tmp_path / "tangle.p"
    pascal.write_text('#include "tangext.h"\nbegin n := argc; end.')

    validator = PascalExtensionValidator(pascal)
    assert validator.header_file == header
    assert validator.check_declaration("argc") is True
