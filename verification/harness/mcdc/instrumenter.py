from verification.harness.mcdc.parser import (
    Node, Expression, Literal, BinaryOp, UnaryOp, Identifier, Assignment,
    ProcedureCall, Block, IfStatement, WhileStatement, RepeatStatement,
    ForStatement, EmptyStatement, Probe, CaseItem, CaseStatement,
    Program, LabelDeclaration, ConstDeclaration, TypeDeclaration, VarDeclaration,
    ProcedureDeclaration, FunctionDeclaration, GotoStatement, LabeledStatement
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
        elif isinstance(node, Program):
            args_str = f"({', '.join(node.args)})" if node.args else ""
            decls_str = "\n".join(self.emit(d) for d in node.declarations)
            return f"PROGRAM {node.name}{args_str};\n{decls_str}\n{self.emit(node.block)}."
        elif isinstance(node, LabelDeclaration):
            return f"LABEL {', '.join(node.labels)};"
        elif isinstance(node, ConstDeclaration):
            consts_str = "; ".join(f"{n} = {self.emit(v)}" for n, v in node.constants)
            return f"CONST {consts_str};"
        elif isinstance(node, TypeDeclaration):
            types_str = "; ".join(f"{n} = {v}" for n, v in node.types)
            return f"TYPE {types_str};"
        elif isinstance(node, VarDeclaration):
            vars_str = "; ".join(f"{', '.join(names)}: {type_name}" for names, type_name in node.vars)
            return f"VAR {vars_str};"
        elif isinstance(node, ProcedureDeclaration):
            res = f"PROCEDURE {node.name}"
            if node.params: res += f"({node.params})"
            res += ";"
            if node.is_forward:
                res += " FORWARD;"
            else:
                if node.declarations:
                    res += "\n" + "\n".join(self.emit(d) for d in node.declarations)
                res += f"\n{self.emit(node.block)};"
            return res
        elif isinstance(node, FunctionDeclaration):
            res = f"FUNCTION {node.name}"
            if node.params: res += f"({node.params})"
            res += f": {node.return_type};"
            if node.is_forward:
                res += " FORWARD;"
            else:
                if node.declarations:
                    res += "\n" + "\n".join(self.emit(d) for d in node.declarations)
                res += f"\n{self.emit(node.block)};"
            return res
        elif isinstance(node, GotoStatement):
            return f"GOTO {node.label}"
        elif isinstance(node, LabeledStatement):
            return f"{node.label}: {self.emit(node.statement)}"
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
        elif isinstance(node, CaseItem):
            labels_str = ", ".join(self.emit(label) for label in node.labels)
            return f"{labels_str}: {self.emit(node.statement)}"
        elif isinstance(node, CaseStatement):
            items_str = "; ".join(self.emit(item) for item in node.items)
            res = f"CASE {self.emit(node.expression)} OF {items_str}"
            if node.otherwise:
                res += f"; OTHERWISE {self.emit(node.otherwise)}"
            res += " END"
            return res
        elif isinstance(node, EmptyStatement):
            return ""
        elif isinstance(node, Probe):
            if node.condition_id is not None:
                return f"mcdc_cond({node.decision_id}, {node.condition_id}, {self.emit(node.value)})"
            return f"mcdc_begin({node.decision_id})"
        else:
            raise ValueError(f"Unknown node type: {type(node)}")

class Instrumenter:
    """Instruments a Pascal AST by inserting Probe nodes."""
    def __init__(self):
        self.next_decision_id = 1
        self.next_condition_id = 1
        self.decisions = {} # decision_id -> instrumented AST node

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

        if isinstance(node, Program):
            return Program(
                node.name,
                node.args,
                [self.instrument(d) for d in node.declarations],
                self.instrument(node.block)
            )

        if isinstance(node, ProcedureDeclaration):
            if node.is_forward: return node
            return ProcedureDeclaration(
                node.name,
                node.params,
                [self.instrument(d) for d in node.declarations],
                self.instrument(node.block)
            )

        if isinstance(node, FunctionDeclaration):
            if node.is_forward: return node
            return FunctionDeclaration(
                node.name,
                node.params,
                node.return_type,
                [self.instrument(d) for d in node.declarations],
                self.instrument(node.block)
            )

        if isinstance(node, LabeledStatement):
            return LabeledStatement(node.label, self.instrument(node.statement))

        if isinstance(node, (IfStatement, WhileStatement, RepeatStatement, ForStatement, CaseStatement)):
            decision_id = self.next_decision_id
            self.next_decision_id += 1
            self.next_condition_id = 1

            if isinstance(node, IfStatement):
                inst_cond = self.instrument_expression(node.condition, decision_id)
                self.decisions[decision_id] = inst_cond
                new_node = IfStatement(
                    inst_cond,
                    self.instrument(node.then_branch),
                    self.instrument(node.else_branch) if node.else_branch else None
                )
            elif isinstance(node, WhileStatement):
                inst_cond = self.instrument_expression(node.condition, decision_id)
                self.decisions[decision_id] = inst_cond
                new_node = WhileStatement(
                    inst_cond,
                    self.instrument(node.body)
                )
            elif isinstance(node, RepeatStatement):
                inst_cond = self.instrument_expression(node.condition, decision_id)
                self.decisions[decision_id] = inst_cond
                new_node = RepeatStatement(
                    [self.instrument(s) for s in node.statements],
                    inst_cond
                )
            elif isinstance(node, CaseStatement):
                # We instrument the expression of the case statement
                inst_expr = self.instrument_expression(node.expression, decision_id)
                self.decisions[decision_id] = inst_expr
                new_node = CaseStatement(
                    inst_expr,
                    [CaseItem(item.labels, self.instrument(item.statement)) for item in node.items],
                    self.instrument(node.otherwise) if node.otherwise else None
                )
            else: # ForStatement
                # ForStatement doesn't have a boolean condition, but we track its execution
                self.decisions[decision_id] = node.variable
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
