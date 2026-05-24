from verification.harness.mcdc.lexer import Token

class Node:
    """Base class for all AST nodes."""
    def __repr__(self):
        return f"{self.__class__.__name__}()"

class Expression(Node):
    """Represents a Pascal expression."""
    def __init__(self, root):
        self.root = root
    def __repr__(self):
        return f"Expr({self.root})"

class Literal(Node):
    """Represents a literal value (number, string)."""
    def __init__(self, value, token_type):
        self.value = value
        self.token_type = token_type
    def __repr__(self):
        if self.token_type == 'STRING':
            return f"'{self.value}'"
        return str(self.value)

class BinaryOp(Node):
    """Represents a binary operation."""
    def __init__(self, left, op, right):
        self.left = left
        self.op = op
        self.right = right
    def __repr__(self):
        return f"({self.left} {self.op} {self.right})"

class UnaryOp(Node):
    """Represents a unary operation."""
    def __init__(self, op, operand):
        self.op = op
        self.operand = operand
    def __repr__(self):
        return f"{self.op}({self.operand})"

class Identifier(Node):
    """Represents a Pascal identifier, potentially with subscripts or dots."""
    def __init__(self, name, modifiers=None):
        self.name = name
        self.modifiers = modifiers or [] # List of ('subscript', indices) or ('dot', name)
    def __repr__(self):
        res = self.name
        for mod_type, val in self.modifiers:
            if mod_type == 'subscript':
                res += f"[{', '.join(repr(idx) for idx in val)}]"
            elif mod_type == 'dot':
                res += f".{val}"
            elif mod_type == 'pointer':
                res += "^"
        return res

class Assignment(Node):
    """Represents an assignment statement."""
    def __init__(self, target, expr):
        self.target = target
        self.expr = expr
    def __repr__(self):
        return f"Assignment({self.target} := {self.expr})"

class ProcedureCall(Node):
    """Represents a procedure call statement."""
    def __init__(self, name, args=None):
        self.name = name
        self.args = args or [] # List of Expression nodes
    def __repr__(self):
        args_str = ", ".join(repr(arg) for arg in self.args)
        return f"ProcedureCall({self.name}({args_str}))"

class Block(Node):
    """Represents a BEGIN...END block."""
    def __init__(self, statements):
        self.statements = statements
    def __repr__(self):
        stmts_str = "; ".join(repr(s) for s in self.statements)
        return f"Block(BEGIN {stmts_str} END)"

class IfStatement(Node):
    """Represents an IF...THEN...ELSE statement."""
    def __init__(self, condition, then_branch, else_branch=None):
        self.condition = condition
        self.then_branch = then_branch
        self.else_branch = else_branch
    def __repr__(self):
        res = f"If({self.condition}) THEN {self.then_branch}"
        if self.else_branch:
            res += f" ELSE {self.else_branch}"
        return res

class WhileStatement(Node):
    """Represents a WHILE...DO statement."""
    def __init__(self, condition, body):
        self.condition = condition
        self.body = body
    def __repr__(self):
        return f"While({self.condition}) DO {self.body}"

class RepeatStatement(Node):
    """Represents a REPEAT...UNTIL statement."""
    def __init__(self, statements, condition):
        self.statements = statements
        self.condition = condition
    def __repr__(self):
        stmts_str = "; ".join(repr(s) for s in self.statements)
        return f"Repeat({stmts_str}) UNTIL {self.condition}"

class ForStatement(Node):
    """Represents a FOR statement."""
    def __init__(self, variable, start_expr, direction, end_expr, body):
        self.variable = variable
        self.start_expr = start_expr
        self.direction = direction # 'TO' or 'DOWNTO'
        self.end_expr = end_expr
        self.body = body
    def __repr__(self):
        return f"For({self.variable} := {self.start_expr} {self.direction} {self.end_expr}) DO {self.body}"

class CaseItem(Node):
    """Represents a single item in a CASE statement."""
    def __init__(self, labels, statement):
        self.labels = labels # List of Expression (usually literals or constants)
        self.statement = statement
    def __repr__(self):
        labels_str = ", ".join(repr(label) for label in self.labels)
        return f"{labels_str}: {self.statement}"

class CaseStatement(Node):
    """Represents a CASE statement."""
    def __init__(self, expression, items, otherwise=None):
        self.expression = expression
        self.items = items
        self.otherwise = otherwise
    def __repr__(self):
        items_str = "; ".join(repr(item) for item in self.items)
        res = f"Case({self.expression}) OF {items_str}"
        if self.otherwise:
            res += f" OTHERWISE {self.otherwise}"
        res += " END"
        return res

class EmptyStatement(Node):
    """Represents an empty statement (e.g., between two semicolons)."""
    def __repr__(self):
        return "EmptyStmt"

class Probe(Node):
    """Represents a coverage probe call."""
    def __init__(self, decision_id, condition_id=None, value=None):
        self.decision_id = decision_id
        self.condition_id = condition_id
        self.value = value

    def __repr__(self):
        if self.condition_id is not None:
            return f"Probe({self.decision_id}, {self.condition_id}, {self.value})"
        return f"Probe({self.decision_id})"

class ParserError(Exception):
    def __init__(self, message, token):
        if token:
            super().__init__(f"{message} at line {token.line}, column {token.column} (token: {token.value})")
        else:
            super().__init__(f"{message} at EOF")
        self.token = token

class Parser:
    """A simple parser for a subset of Pascal."""

    def __init__(self, tokens):
        self.tokens = [t for t in tokens if t.type != 'COMMENT']
        self.pos = 0

    def peek(self, offset=0):
        if self.pos + offset < len(self.tokens):
            return self.tokens[self.pos + offset]
        return None

    def consume(self, expected=None):
        token = self.peek()
        if token is None:
            raise ParserError("Unexpected end of input", None)
        if expected:
            if isinstance(expected, str) and token.type != expected:
                raise ParserError(f"Expected token type {expected}, got {token.type}", token)
            elif isinstance(expected, list) and token.type not in expected:
                raise ParserError(f"Expected one of {expected}, got {token.type}", token)
        self.pos += 1
        return token

    def parse_identifier(self):
        """Parses an identifier with potential subscripts and dots."""
        id_token = self.consume('ID')
        name = id_token.value
        modifiers = []

        while True:
            nxt = self.peek()
            if nxt is None: break

            if nxt.value == '[':
                self.consume() # [
                indices = []
                while True:
                    idx = self.parse_expression_internal()
                    indices.append(Expression(idx))
                    if self.peek() and self.peek().value == ',':
                        self.consume()
                    else:
                        break
                if self.peek() and self.peek().value == ']':
                    self.consume()
                else:
                    raise ParserError("Expected ']'", self.peek())
                modifiers.append(('subscript', indices))
            elif nxt.value == '.':
                self.consume() # .
                dot_id = self.consume('ID')
                modifiers.append(('dot', dot_id.value))
            elif nxt.value == '^':
                self.consume() # ^ (pointer dereference)
                modifiers.append(('pointer', None))
            else:
                break
        return Identifier(name, modifiers)

    def parse_expression(self):
        """Parses an expression."""
        return Expression(self.parse_expression_internal())

    def parse_expression_internal(self):
        """Pascal expression: simple_expression {relop simple_expression}"""
        left = self.parse_simple_expression()
        while self.peek() and (self.peek().value in ('=', '<>', '<', '<=', '>', '>=') or self.peek().type == 'IN'):
            op = self.consume().value
            right = self.parse_simple_expression()
            left = BinaryOp(left, op, right)
        return left

    def parse_simple_expression(self):
        """Pascal simple_expression: [sign] term {addop term}"""
        nxt = self.peek()
        if nxt and nxt.value in ('+', '-'):
            op = self.consume().value
            left = UnaryOp(op, self.parse_term())
        else:
            left = self.parse_term()

        while self.peek() and (self.peek().value in ('+', '-') or self.peek().type == 'OR'):
            op = self.consume().value
            right = self.parse_term()
            left = BinaryOp(left, op, right)
        return left

    def parse_term(self):
        """Pascal term: factor {mulop factor}"""
        left = self.parse_factor()
        while self.peek() and (self.peek().value in ('*', '/') or self.peek().type in ('DIV', 'MOD', 'AND')):
            op = self.consume().value
            right = self.parse_factor()
            left = BinaryOp(left, op, right)
        return left

    def parse_factor(self):
        """Pascal factor: identifier | identifier '(' args ')' | literal | '(' expression ')' | NOT factor"""
        token = self.peek()
        if token is None:
            raise ParserError("Unexpected end of expression", None)

        if token.value == '(':
            self.consume()
            expr = self.parse_expression_internal()
            if self.peek() and self.peek().value == ')':
                self.consume()
            else:
                raise ParserError("Expected ')'", self.peek())
            return expr
        elif token.type == 'NOT':
            self.consume()
            return UnaryOp('NOT', self.parse_factor())
        elif token.type in ('NUMBER', 'STRING'):
            t = self.consume()
            return Literal(t.value, t.type)
        elif token.type == 'ID':
            id_node = self.parse_identifier()
            if self.peek() and self.peek().value == '(':
                args = self.parse_args()
                return ProcedureCall(id_node, args)
            return id_node
        else:
            raise ParserError(f"Unexpected token {token.value} in expression", token)

    def parse_args(self):
        """Parses procedure call arguments."""
        self.consume() # (
        args = []
        if self.peek() and self.peek().value == ')':
            self.consume() # )
            return args

        while True:
            arg_expr = self.parse_expression()
            args.append(arg_expr)
            nxt = self.peek()
            if nxt and nxt.value == ')':
                self.consume()
                break
            elif nxt and nxt.value == ',':
                self.consume()
            else:
                raise ParserError(f"Expected ',' or ')', got {nxt.value if nxt else 'EOF'}", nxt)
        return args

    def parse_block(self):
        """Parses a BEGIN...END block."""
        self.consume('BEGIN')
        statements = []
        while self.peek() and self.peek().type != 'END':
            last_pos = self.pos
            stmt = self.parse_statement()
            if stmt:
                statements.append(stmt)
            if self.peek() and self.peek().value == ';':
                self.consume()

            if self.pos == last_pos:
                raise ParserError("Parser failed to progress in BEGIN...END block", self.peek())
        self.consume('END')
        return Block(statements)

    def parse_if_statement(self):
        """Parses an IF...THEN...ELSE statement."""
        self.consume('IF')
        condition = self.parse_expression()
        self.consume('THEN')
        then_branch = self.parse_statement()
        else_branch = None
        if self.peek() and self.peek().type == 'ELSE':
            self.consume('ELSE')
            else_branch = self.parse_statement()
        return IfStatement(condition, then_branch, else_branch)

    def parse_while_statement(self):
        """Parses a WHILE...DO statement."""
        self.consume('WHILE')
        condition = self.parse_expression()
        self.consume('DO')
        body = self.parse_statement()
        return WhileStatement(condition, body)

    def parse_repeat_statement(self):
        """Parses a REPEAT...UNTIL statement."""
        self.consume('REPEAT')
        statements = []
        while self.peek() and self.peek().type != 'UNTIL':
            last_pos = self.pos
            stmt = self.parse_statement()
            if stmt:
                statements.append(stmt)
            if self.peek() and self.peek().value == ';':
                self.consume()
            if self.pos == last_pos:
                 raise ParserError("Parser failed to progress in REPEAT...UNTIL block", self.peek())
        self.consume('UNTIL')
        condition = self.parse_expression()
        return RepeatStatement(statements, condition)

    def parse_for_statement(self):
        """Parses a FOR statement."""
        self.consume('FOR')
        variable = self.parse_identifier()
        self.consume('ASSIGN')
        start_expr = self.parse_expression()
        direction = self.consume(['TO', 'DOWNTO']).type
        end_expr = self.parse_expression()
        self.consume('DO')
        body = self.parse_statement()
        return ForStatement(variable, start_expr, direction, end_expr, body)

    def parse_case_statement(self):
        """Parses a CASE statement."""
        self.consume('CASE')
        expression = self.parse_expression()
        self.consume('OF')
        items = []
        otherwise = None

        while self.peek() and self.peek().type not in ('END', 'OTHERWISE'):
            labels = []
            while True:
                labels.append(self.parse_expression())
                if self.peek() and self.peek().value == ',':
                    self.consume()
                else:
                    break
            self.consume('OP') # :
            stmt = self.parse_statement()
            items.append(CaseItem(labels, stmt))
            if self.peek() and self.peek().value == ';':
                self.consume()

        if self.peek() and self.peek().type == 'OTHERWISE':
            self.consume()
            otherwise = self.parse_statement()
            if self.peek() and self.peek().value == ';':
                self.consume()

        self.consume('END')
        return CaseStatement(expression, items, otherwise)

    def parse_statement(self):
        """Parses a single statement."""
        # Skip labels
        while self.peek() and self.peek().type == 'NUMBER' and self.peek(1) and self.peek(1).value == ':':
            self.consume() # number
            self.consume() # :

        token = self.peek()
        if token is None: return None

        if token.type == 'BEGIN':
            return self.parse_block()
        elif token.type == 'IF':
            return self.parse_if_statement()
        elif token.type == 'WHILE':
            return self.parse_while_statement()
        elif token.type == 'REPEAT':
            return self.parse_repeat_statement()
        elif token.type == 'FOR':
            return self.parse_for_statement()
        elif token.type == 'CASE':
            return self.parse_case_statement()
        elif token.value == ';':
            return EmptyStatement()
        elif token.type == 'END' or token.type == 'ELSE' or token.type == 'UNTIL':
             # Statements can be empty before these tokens
             return EmptyStatement()
        elif token.type == 'ID':
            # Lookahead to distinguish assignment and call
            # We need to parse identifier first because of subscripts/dots
            start_pos = self.pos
            try:
                target = self.parse_identifier()
                nxt = self.peek()
                if nxt and nxt.type == 'ASSIGN':
                    self.consume('ASSIGN')
                    expr = self.parse_expression()
                    return Assignment(target, expr)
                else:
                    # Procedure call
                    args = []
                    if nxt and nxt.value == '(':
                        args = self.parse_args()
                    return ProcedureCall(target, args)
            except ParserError:
                # Backtrack if it wasn't a simple ID-led statement
                self.pos = start_pos
                raise

        # For now, just raise if we encounter something else we haven't implemented
        raise ParserError(f"Statement type {token.type} ({token.value}) not implemented", token)
