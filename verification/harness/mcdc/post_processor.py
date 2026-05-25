import collections

def parse_mcdc_log(filepath):
    """
    Parses the MC/DC coverage log file and groups evaluations by decision ID.

    :param filepath: Path to the mcdc_coverage.out file.
    :return: Dictionary mapping decision_id to a list of test vectors (dicts).
    """
    decisions = collections.defaultdict(list)
    # Since we don't have mcdc_end, we flush a vector when mcdc_begin for the SAME id is seen,
    # or when the log ends.
    # Nested decisions with different IDs are handled by keeping them separate.
    pending_vectors = {} # decision_id -> current_vector dict

    try:
        with open(filepath, 'r') as f:
            for line in f:
                parts = line.strip().split()
                if not parts:
                    continue

                type = parts[0]
                if type == 'B':
                    d_id = int(parts[1])
                    if d_id in pending_vectors:
                        # Flush previous evaluation of this decision
                        if pending_vectors[d_id]:
                            decisions[d_id].append(pending_vectors[d_id])
                    pending_vectors[d_id] = {}
                elif type == 'C':
                    d_id = int(parts[1])
                    c_id = int(parts[2])
                    val = parts[3] == '1'

                    if d_id not in pending_vectors:
                        # Should not happen with correct instrumentation
                        pending_vectors[d_id] = {}

                    pending_vectors[d_id][c_id] = val
    except FileNotFoundError:
        print(f"Warning: {filepath} not found.")
        return {}

    # Flush all remaining pending vectors
    for d_id, vector in pending_vectors.items():
        if vector:
            decisions[d_id].append(vector)

    return dict(decisions)

def merge_mcdc_results(all_results_list):
    """
    Merges multiple MC/DC result dictionaries.

    :param all_results_list: List of dictionaries returned by parse_mcdc_log.
    :return: Merged dictionary mapping decision_id to list of all test vectors.
    """
    merged = collections.defaultdict(list)
    for results in all_results_list:
        for d_id, vectors in results.items():
            merged[d_id].extend(vectors)
    return dict(merged)
