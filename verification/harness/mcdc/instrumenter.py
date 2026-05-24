from verification.harness.mcdc.parser import (
    Node, Block, IfStatement, WhileStatement, RepeatStatement, ForStatement,
    Probe, Assignment, ProcedureCall, EmptyStatement
)

class Instrumenter:
    """Inserts coverage probes into the Pascal AST."""

    def __init__(self):
        self.probe_count = 0

    def next_probe(self):
        self.probe_count += 1
        return Probe(self.probe_count)

    def instrument(self, node):
        """Top-level entry point to instrument an AST or list of statements."""
        if isinstance(node, list):
            return [self.visit(stmt) for stmt in node]
        return self.visit(node)

    def wrap_in_block(self, stmt):
        """Ensures a statement is a Block, and prepends a probe."""
        probe = self.next_probe()
        if isinstance(stmt, Block):
            return Block([probe] + self.instrument_list(stmt.statements))
        elif isinstance(stmt, EmptyStatement):
            return Block([probe])
        else:
            return Block([probe, self.visit(stmt)])

    def instrument_list(self, statements):
        """Instruments a list of statements."""
        return [self.visit(s) for s in statements]

    def visit(self, node):
        """Recursive visitor to instrument nodes."""
        if isinstance(node, IfStatement):
            then_branch = self.wrap_in_block(node.then_branch)
            else_branch = None
            if node.else_branch:
                else_branch = self.wrap_in_block(node.else_branch)
            else:
                # Even if there is no ELSE, MC/DC needs to know if the branch was NOT taken.
                # So we add an implicit ELSE with a probe.
                else_branch = Block([self.next_probe()])
            return IfStatement(node.condition, then_branch, else_branch)

        elif isinstance(node, WhileStatement):
            body = self.wrap_in_block(node.body)
            return WhileStatement(node.condition, body)

        elif isinstance(node, ForStatement):
            body = self.wrap_in_block(node.body)
            return ForStatement(node.variable, node.start_expr, node.direction, node.end_expr, body)

        elif isinstance(node, RepeatStatement):
            probe = self.next_probe()
            # REPEAT...UNTIL body is always a list of statements in our AST
            instrumented_body = [probe] + self.instrument_list(node.statements)
            return RepeatStatement(instrumented_body, node.condition)

        elif isinstance(node, Block):
            return Block(self.instrument_list(node.statements))

        # Leaf nodes or non-decision statements
        return node
