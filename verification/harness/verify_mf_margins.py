import re
import os
import logging
from pathlib import Path

def extract_web_definition(web_content, name):
    """
    Extracts the value of a WEB definition (@d) or constant.
    Handles simple numeric values and expressions of already defined names.
    """
    # Regex for @d name=value or @!name=value;
    # WEB definitions: @d name=value
    pattern = rf"@d\s+{name}\s*=\s*([^@\s{{;]+)"
    match = re.search(pattern, web_content)
    if not match:
        # Try constant pattern: @!name=value;
        pattern = rf"@!\s*{name}\s*=\s*([^@\s{{;]+)"
        match = re.search(pattern, web_content)

    if match:
        return match.group(1).strip()
    return None

def verify_mf_margins(web_path):
    """
    Verifies Metafont bisection stack safety margins.
    """
    if not os.path.exists(web_path):
        raise FileNotFoundError(f"WEB file not found: {web_path}")

    with open(web_path, 'r') as f:
        content = f.read()

    move_increment_str = extract_web_definition(content, "move_increment")
    int_packets_str = extract_web_definition(content, "int_packets")
    bistack_size_str = extract_web_definition(content, "bistack_size")

    if not all([move_increment_str, int_packets_str, bistack_size_str]):
        return False, f"Failed to extract all required constants: move_increment={move_increment_str}, int_packets={int_packets_str}, bistack_size={bistack_size_str}"

    try:
        move_increment = int(move_increment_str)
        int_packets = int(int_packets_str)
        bistack_size = int(bistack_size_str)
    except ValueError as e:
        return False, f"Failed to parse constants as integers: {e}"

    # int_increment is defined as int_packets+int_packets+5
    int_increment_expr = extract_web_definition(content, "int_increment")
    if not int_increment_expr:
        return False, "Failed to extract int_increment expression"

    # Simple evaluator for the specific expression int_packets+int_packets+5
    # Replace known variable names with their values
    eval_expr = int_increment_expr.replace("int_packets", str(int_packets))
    try:
        # Safe eval for simple arithmetic
        int_increment = eval(eval_expr, {"__builtins__": None}, {})
    except Exception as e:
        return False, f"Failed to evaluate int_increment expression '{int_increment_expr}': {e}"

    errors = []
    # Check bad=31
    if 15 * move_increment > bistack_size:
        errors.append(f"Safety check bad=31 failed: 15 * move_increment ({15 * move_increment}) > bistack_size ({bistack_size})")

    # Check bad=32
    if int_packets + 17 * int_increment > bistack_size:
        errors.append(f"Safety check bad=32 failed: int_packets + 17 * int_increment ({int_packets + 17 * int_increment}) > bistack_size ({bistack_size})")

    if errors:
        return False, "; ".join(errors)

    return True, "All bisection stack safety margins are maintained."

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    success, message = verify_mf_margins("dist/mf/mf.web")
    if success:
        logging.info(message)
        exit(0)
    else:
        logging.error(message)
        exit(1)
