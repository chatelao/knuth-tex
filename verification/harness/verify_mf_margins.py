import re
import sys
from pathlib import Path

def parse_web_constants(web_path):
    content = Path(web_path).read_text()

    # Extract bistack_size
    # Pattern: @!bistack_size=785;
    bistack_size_match = re.search(r'@!bistack_size=(\d+);', content)
    bistack_size = int(bistack_size_match.group(1)) if bistack_size_match else None

    # Extract move_increment
    # Pattern: @d move_increment=11
    move_increment_match = re.search(r'@d move_increment=(\d+)', content)
    move_increment = int(move_increment_match.group(1)) if move_increment_match else None

    # Extract int_packets
    # Pattern: @d int_packets=20
    int_packets_match = re.search(r'@d int_packets=(\d+)', content)
    int_packets = int(int_packets_match.group(1)) if int_packets_match else None

    # Extract int_increment
    # Pattern: @d int_increment=int_packets+int_packets+5
    # We might need to handle the expression
    int_increment_match = re.search(r'@d int_increment=([^ \n\{]+)', content)
    int_increment_raw = int_increment_match.group(1) if int_increment_match else None

    int_increment = None
    if int_increment_raw:
        if int_increment_raw.isdigit():
            int_increment = int(int_increment_raw)
        elif "int_packets" in int_increment_raw and int_packets is not None:
            # Simple replacement for this specific case
            expr = int_increment_raw.replace("int_packets", str(int_packets))
            # Basic eval-like behavior for +, -, *
            # For simplicity, we just handle the known case: int_packets+int_packets+5
            try:
                int_increment = eval(expr)
            except:
                pass

    return {
        "bistack_size": bistack_size,
        "move_increment": move_increment,
        "int_packets": int_packets,
        "int_increment": int_increment
    }

def verify_margins(constants):
    bistack_size = constants["bistack_size"]
    move_increment = constants["move_increment"]
    int_packets = constants["int_packets"]
    int_increment = constants["int_increment"]

    if None in [bistack_size, move_increment, int_packets, int_increment]:
        print("Error: Could not extract all constants.")
        print(constants)
        return False

    print(f"Constants found: bistack_size={bistack_size}, move_increment={move_increment}, int_packets={int_packets}, int_increment={int_increment}")

    success = True

    # bad=31: if 15*move_increment>bistack_size then bad:=31;
    if 15 * move_increment > bistack_size:
        print(f"FAILED: 15 * move_increment ({15 * move_increment}) > bistack_size ({bistack_size}) [bad=31]")
        success = False
    else:
        print(f"PASSED: 15 * move_increment ({15 * move_increment}) <= bistack_size ({bistack_size})")

    # bad=32: if int_packets+17*int_increment>bistack_size then bad:=32;
    if int_packets + 17 * int_increment > bistack_size:
        print(f"FAILED: int_packets + 17 * int_increment ({int_packets + 17 * int_increment}) > bistack_size ({bistack_size}) [bad=32]")
        success = False
    else:
        print(f"PASSED: int_packets + 17 * int_increment ({int_packets + 17 * int_increment}) <= bistack_size ({bistack_size})")

    return success

if __name__ == "__main__":
    web_file = "dist/mf/mf.web"
    if len(sys.argv) > 1:
        web_file = sys.argv[1]

    constants = parse_web_constants(web_file)
    if verify_margins(constants):
        print("Metafont bisection stack safety margins verified.")
        sys.exit(0)
    else:
        print("Metafont bisection stack safety margins VIOLATION detected.")
        sys.exit(1)
