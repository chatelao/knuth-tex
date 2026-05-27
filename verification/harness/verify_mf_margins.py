import re
import sys

def verify_margins(web_file):
    with open(web_file, 'r') as f:
        content = f.read()

    # Extract constants using regex
    # @!bistack_size=785;
    bistack_match = re.search(r'@!bistack_size=(\d+);', content)
    # @d move_increment=11
    move_inc_match = re.search(r'@d move_increment=(\d+)', content)
    # @d int_packets=20
    int_packets_match = re.search(r'@d int_packets=(\d+)', content)
    # @d int_increment=int_packets+int_packets+5
    # Since int_increment depends on int_packets, we need to handle that.
    int_inc_match = re.search(r'@d int_increment=int_packets\+int_packets\+(\d+)', content)

    if not all([bistack_match, move_inc_match, int_packets_match, int_inc_match]):
        print("Failed to find all constants in mf.web")
        return False

    bistack_size = int(bistack_match.group(1))
    move_increment = int(move_inc_match.group(1))
    int_packets = int(int_packets_match.group(1))
    int_increment_offset = int(int_inc_match.group(1))
    int_increment = 2 * int_packets + int_increment_offset

    print(f"Constants found in {web_file}:")
    print(f"  bistack_size = {bistack_size}")
    print(f"  move_increment = {move_increment}")
    print(f"  int_packets = {int_packets}")
    print(f"  int_increment = {int_increment}")

    # Safety margin checks (bad=31, 32)
    # bad=31: if 15*move_increment>bistack_size then bad:=31;
    margin31 = 15 * move_increment
    # bad=32: if int_packets+17*int_increment>bistack_size then bad:=32;
    margin32 = int_packets + 17 * int_increment

    print("\nSafety Margin Checks:")
    print(f"  bad=31 margin: 15 * {move_increment} = {margin31} (<= {bistack_size})")
    print(f"  bad=32 margin: {int_packets} + 17 * {int_increment} = {margin32} (<= {bistack_size})")

    success = True
    if margin31 > bistack_size:
        print("ERROR: Safety margin for bad=31 violated!")
        success = False
    if margin32 > bistack_size:
        print("ERROR: Safety margin for bad=32 violated!")
        success = False

    if success:
        print("\nAll bisection stack safety margins are maintained.")
    return success

if __name__ == "__main__":
    web_path = "dist/mf/mf.web"
    if len(sys.argv) > 1:
        web_path = sys.argv[1]

    if not verify_margins(web_path):
        sys.exit(1)
