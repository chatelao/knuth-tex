from verification.harness.mcdc.parser import (
    Node, Expression, Literal, BinaryOp, UnaryOp, Identifier, Assignment,
    ProcedureCall, Block, IfStatement, WhileStatement, RepeatStatement,
    ForStatement, EmptyStatement, Probe
)

class PascalEmitter:
    """Converts AST nodes back into Pascal source code."""
    def emit(self, node):
        if node is None:
            return ""
        if isinstance(node, Expression):
            return self.emit(node.root)
        elif isinstance(node, Literal):
            if node.token_type == 'STRING':
                return f"'{node.value}'"
            return str(node.value)
        elif isinstance(node, BinaryOp):
            return f"({self.emit(node.left)} {node.op} {self.emit(node.right)})"
        elif isinstance(node, UnaryOp):
            if node.op.upper() == 'NOT':
                 return f"NOT {self.emit(node.operand)}"
            return f"{node.op}{self.emit(node.operand)}"
        elif isinstance(node, Identifier):
            res = node.name
            for mod_type, val in node.modifiers:
                if mod_type == 'subscript':
                    res += f"[{', '.join(self.emit(idx) for idx in val)}]"
                elif mod_type == 'dot':
                    res += f".{val}"
                elif mod_type == 'pointer':
                    res += "^"
            return res
        elif isinstance(node, Assignment):
            return f"{self.emit(node.target)} := {self.emit(node.expr)}"
        elif isinstance(node, ProcedureCall):
            name_str = self.emit(node.name)
            if not node.args:
                return name_str
            args_str = ", ".join(self.emit(arg) for arg in node.args)
            return f"{name_str}({args_str})"
        elif isinstance(node, Block):
            stmts = [self.emit(s) for s in node.statements]
            stmts = [s for s in stmts if s]
            return f"BEGIN {'; '.join(stmts)} END"
        elif isinstance(node, IfStatement):
            res = f"IF {self.emit(node.condition)} THEN {self.emit(node.then_branch)}"
            if node.else_branch:
                res += f" ELSE {self.emit(node.else_branch)}"
            return res
        elif isinstance(node, WhileStatement):
            return f"WHILE {self.emit(node.condition)} DO {self.emit(node.body)}"
        elif isinstance(node, RepeatStatement):
            stmts = [self.emit(s) for s in node.statements]
            stmts = [s for s in stmts if s]
            return f"REPEAT {'; '.join(stmts)} UNTIL {self.emit(node.condition)}"
        elif isinstance(node, ForStatement):
            return f"FOR {self.emit(node.variable)} := {self.emit(node.start_expr)} {node.direction} {self.emit(node.end_expr)} DO {self.emit(node.body)}"
        elif isinstance(node, EmptyStatement):
            return ""
        elif isinstance(node, Probe):
            if node.condition_id is not None:
                return f"record_mcdc({node.decision_id}, {node.condition_id}, {self.emit(node.value)})"
            return f"record_mcdc({node.decision_id})"
        else:
            raise ValueError(f"Unknown node type: {type(node)}")

class Instrumenter:
    """Instruments a Pascal AST by inserting Probe nodes."""
    def __init__(self):
        self.next_decision_id = 1
        self.next_condition_id = 1

    def instrument(self, node):
        if isinstance(node, Block):
            new_statements = []
            for stmt in node.statements:
                instrumented = self.instrument(stmt)
                if isinstance(instrumented, Block) and not isinstance(stmt, Block):
                     # Flatten if it was wrapped in a block by our instrumentation
                     new_statements.extend(instrumented.statements)
                else:
                     new_statements.append(instrumented)
            return Block(new_statements)

        if isinstance(node, (IfStatement, WhileStatement, RepeatStatement, ForStatement)):
            decision_id = self.next_decision_id
            self.next_decision_id += 1
            self.next_condition_id = 1

            if isinstance(node, IfStatement):
                new_node = IfStatement(
                    self.instrument_expression(node.condition, decision_id),
                    self.instrument(node.then_branch),
                    self.instrument(node.else_branch) if node.else_branch else None
                )
            elif isinstance(node, WhileStatement):
                new_node = WhileStatement(
                    self.instrument_expression(node.condition, decision_id),
                    self.instrument(node.body)
                )
            elif isinstance(node, RepeatStatement):
                new_node = RepeatStatement(
                    [self.instrument(s) for s in node.statements],
                    self.instrument_expression(node.condition, decision_id)
                )
            else: # ForStatement
                new_node = ForStatement(
                    node.variable,
                    node.start_expr,
                    node.direction,
                    node.end_expr,
                    self.instrument(node.body)
                )

            return Block([Probe(decision_id), new_node])

        return node

    def instrument_expression(self, expr, decision_id):
        if isinstance(expr, Expression):
            return Expression(self.instrument_expression(expr.root, decision_id))

        if isinstance(expr, BinaryOp) and expr.op.upper() in ('AND', 'OR'):
            return BinaryOp(
                self.instrument_expression(expr.left, decision_id),
                expr.op,
                self.instrument_expression(expr.right, decision_id)
            )

        if isinstance(expr, UnaryOp) and expr.op.upper() == 'NOT':
            return UnaryOp(
                expr.op,
                self.instrument_expression(expr.operand, decision_id)
            )

        # Atomic condition
        cond_id = self.next_condition_id
        self.next_condition_id += 1
        return Probe(decision_id, cond_id, expr)
