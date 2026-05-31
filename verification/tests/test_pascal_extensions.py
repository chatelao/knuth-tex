import pytest
import os
import re
from pathlib import Path
from verification.harness.verify_pascal_extensions import PascalExtensionValidator
from verification.harness.verify_tangle_output import PascalNormalizer

def verify_extension_usage(pascal_file, extensions, required_usage=None, required_declaration=None):
    if not os.path.exists(pascal_file):
        pytest.skip(f"Pascal file not found: {pascal_file}")

    if required_usage is None:
        required_usage = extensions
    if required_declaration is None:
        required_declaration = extensions

    validator = PascalExtensionValidator(pascal_file)
    for ext in extensions:
        declared, used = validator.verify_extension(ext)
        if ext in required_declaration:
            assert declared, f"Extension {ext} not declared for {pascal_file}"
        if ext in required_usage:
            assert used, f"Extension {ext} not used in {pascal_file}"

def test_tangle_extensions():
    verify_extension_usage('local/web/tangle.p', ['argc', 'argv', 'flushstdout', 'lineread', 'testeof', 'exit'])

def test_weave_extensions():
    verify_extension_usage('local/web/weave.p', ['argc', 'argv', 'flushstdout', 'lineread', 'testeof', 'exit'])

def test_tangle_sparc_extensions():
    verify_extension_usage(
        'local/web-sparc/tangle.p',
        ['argc', 'argv', 'lineread', 'linewrite', 'testeof', 'exit'],
        required_declaration=['lineread', 'linewrite', 'testeof', 'exit']
    )

def test_vftovp_extensions():
    verify_extension_usage('local/etc/vftovp.p', ['argc', 'argv', 'flushstdout', 'setpaths', 'testaccess'], required_usage=['argc', 'argv', 'setpaths', 'testaccess'])

def test_vptovf_extensions():
    verify_extension_usage('local/etc/vptovf.p', ['argc', 'argv'], required_usage=['argc', 'argv'])

def test_pltotf_extensions():
    # Use glob to find the correct path as it might vary (e.g., local/texware/ or local/texware-sparc/)
    paths = list(Path('local').rglob('pltotf.p'))
    if not paths:
        pytest.skip("pltotf.p not found")
    verify_extension_usage(str(paths[0]), ['argc', 'argv'], required_usage=['argc', 'argv'])

def test_tftopl_extensions():
    paths = list(Path('local').rglob('tftopl.p'))
    if not paths:
        pytest.skip("tftopl.p not found")
    verify_extension_usage(str(paths[0]), ['argc', 'argv'], required_usage=['argc', 'argv'])

def test_dvitype_extensions():
    paths = list(Path('local').rglob('dvitype.p'))
    if not paths:
        pytest.skip("dvitype.p not found")
    verify_extension_usage(str(paths[0]), ['argc', 'argv', 'flushstdout', 'setpaths', 'testaccess'])

def test_gftodvi_extensions():
    verify_extension_usage('local/mfware/gftodvi.p', ['argc', 'argv', 'flushstdout', 'setpaths', 'testaccess'])

def test_pooltype_extensions():
    verify_extension_usage('local/texware/pooltype.p', ['argc', 'argv'])

def test_pascal_labels():
    """
    Verifies that all label declarations in Pascal files are within the standard range (1-9999).
    """
    pascal_files = list(Path('local').rglob('*.p'))
    # Matches label declarations. We catch all text until the semicolon to verify it.
    label_pattern = re.compile(r'\blabel\b\s*([^;]+);', re.IGNORECASE)
    normalizer = PascalNormalizer()

    for p_file in pascal_files:
        # Skip binary files if any
        try:
            with open(p_file, 'r', encoding='utf-8') as f:
                content = f.read()
        except UnicodeDecodeError:
            continue

        # Strip comments and strings to avoid matching them in label lists
        clean_content = normalizer.strip_strings(normalizer.strip_comments(content))

        matches = label_pattern.findall(clean_content)
        for label_group in matches:
            # Labels can be comma-separated: label 10, 20, 30;
            labels = [l.strip() for l in label_group.split(',')]
            for label in labels:
                if not label: continue
                # Verify it is numeric and within range
                assert label.isdigit(), f"Non-numeric label '{label}' found in {p_file}. Group: {label_group}"
                val = int(label)
                assert 1 <= val <= 9999, f"Label '{label}' out of standard range (1-9999) in {p_file}"
