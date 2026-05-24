from verification.harness.mcdc.parser import BinaryOp, UnaryOp, Probe, Expression

class MCDCAnalyzer:
    """Analyzes MC/DC coverage for a decision based on observed test vectors."""

    def __init__(self, expression_ast):
        """
        Initialize with the instrumented AST of the decision expression.
        :param expression_ast: The AST node (usually Expression or BinaryOp/UnaryOp/Probe).
        """
        if isinstance(expression_ast, Expression):
            self.ast = expression_ast.root
        else:
            self.ast = expression_ast
        self.condition_ids = self._extract_condition_ids(self.ast)

    def _extract_condition_ids(self, node):
        ids = set()
        if isinstance(node, Probe):
            if node.condition_id is not None:
                ids.add(node.condition_id)
        elif isinstance(node, BinaryOp):
            ids.update(self._extract_condition_ids(node.left))
            ids.update(self._extract_condition_ids(node.right))
        elif isinstance(node, UnaryOp):
            ids.update(self._extract_condition_ids(node.operand))
        return ids

    def evaluate(self, node, vector):
        """
        Evaluates the expression for a given test vector.
        :param node: AST node to evaluate.
        :param vector: Dictionary mapping condition_id to boolean value.
        """
        if isinstance(node, Probe):
            if node.condition_id is not None:
                return vector[node.condition_id]
            else:
                # This should not happen in an instrumented expression used for MC/DC
                raise ValueError("Encountered Probe without condition_id during evaluation")

        if isinstance(node, BinaryOp):
            left = self.evaluate(node.left, vector)
            right = self.evaluate(node.right, vector)
            op = node.op.upper()
            if op == 'AND':
                return left and right
            if op == 'OR':
                return left or right
            # For MC/DC we mostly care about AND/OR/NOT, but we should handle others if they appear
            # though usually they are wrapped in Probes as atomic conditions.
            if op == '=': return left == right
            if op == '<>': return left != right
            if op == '<': return left < right
            if op == '<=': return left <= right
            if op == '>': return left > right
            if op == '>=': return left >= right
            if op == '+': return left + right
            if op == '-': return left - right
            if op == '*': return left * right
            if op == '/': return left / right
            if op == 'DIV': return left // right
            if op == 'MOD': return left % right
            raise ValueError(f"Unsupported operator in evaluation: {op}")

        if isinstance(node, UnaryOp):
            val = self.evaluate(node.operand, vector)
            op = node.op.upper()
            if op == 'NOT':
                return not val
            if op == '+':
                return val
            if op == '-':
                return -val
            raise ValueError(f"Unsupported unary operator: {op}")

        # Literal or Identifier (should be inside a Probe if instrumented correctly)
        if hasattr(node, 'value'):
            return node.value

        raise ValueError(f"Unsupported node type for evaluation: {type(node)}")

    def analyze(self, test_vectors):
        """
        Analyzes the test vectors for MC/DC coverage.
        :param test_vectors: A list of dictionaries, each mapping condition_id to bool.
        :return: A dictionary containing coverage results.
        """
        results = {
            'decision_id': getattr(self.ast, 'decision_id', None) if isinstance(self.ast, Probe) else None,
            'conditions': {},
            'total_conditions': len(self.condition_ids),
            'covered_conditions': 0,
            'mcdc_percentage': 0.0
        }

        # If the root is not a Probe, we try to find one to get the decision_id
        if results['decision_id'] is None:
            def find_decision_id(node):
                if isinstance(node, Probe): return node.decision_id
                if isinstance(node, BinaryOp): return find_decision_id(node.left) or find_decision_id(node.right)
                if isinstance(node, UnaryOp): return find_decision_id(node.operand)
                return None
            results['decision_id'] = find_decision_id(self.ast)

        # Unique vectors
        unique_vectors = []
        seen = set()
        for v in test_vectors:
            tuple_v = tuple(sorted(v.items()))
            if tuple_v not in seen:
                seen.add(tuple_v)
                unique_vectors.append(v)

        for cond_id in sorted(self.condition_ids):
            independence_pair = self._find_independence_pair(cond_id, unique_vectors)
            results['conditions'][cond_id] = {
                'covered': independence_pair is not None,
                'independence_pair': independence_pair
            }
            if independence_pair:
                results['covered_conditions'] += 1

        if results['total_conditions'] > 0:
            results['mcdc_percentage'] = (results['covered_conditions'] / results['total_conditions']) * 100

        return results

    def _find_independence_pair(self, cond_id, vectors):
        """
        Finds a pair of vectors that demonstrate the independent effect of cond_id.
        """
        for i, v1 in enumerate(vectors):
            for v2 in vectors[i+1:]:
                # Check if they differ only in cond_id
                diff_keys = [k for k in self.condition_ids if v1.get(k) != v2.get(k)]
                if diff_keys == [cond_id]:
                    # They differ only in cond_id. Now check decision outcome.
                    if self.evaluate(self.ast, v1) != self.evaluate(self.ast, v2):
                        return (v1, v2)
        return None
