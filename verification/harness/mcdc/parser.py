from verification.harness.mcdc.lexer import Token

class Node:
    """Base class for all AST nodes."""
    def __repr__(self):
        return f"{self.__class__.__name__}()"

class Expression(Node):
    """Represents a Pascal expression."""
    def __init__(self, tokens):
        self.tokens = tokens
    def __repr__(self):
        return f"Expr('{' '.join(t.value for t in self.tokens)}')"

class Identifier(Node):
    """Represents a Pascal identifier, potentially with subscripts or dots."""
    def __init__(self, name, modifiers=None):
        self.name = name
        self.modifiers = modifiers or [] # List of ('subscript', [tokens]) or ('dot', name)
    def __repr__(self):
        res = self.name
        for mod_type, val in self.modifiers:
            if mod_type == 'subscript':
                res += f"[{' '.join(t.value for t in val)}]"
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
                sub_tokens = []
                bracket_level = 1
                while bracket_level > 0:
                    t = self.consume()
                    if t.value == '[': bracket_level += 1
                    elif t.value == ']': bracket_level -= 1
                    if bracket_level > 0:
                        sub_tokens.append(t)
                modifiers.append(('subscript', sub_tokens))
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

    def parse_expression(self, delimiters):
        """Parses an expression until one of the delimiters is reached (balancing parens)."""
        expr_tokens = []
        paren_level = 0
        bracket_level = 0

        while True:
            nxt = self.peek()
            if nxt is None: break

            if paren_level == 0 and bracket_level == 0:
                if nxt.type in delimiters or nxt.value in delimiters:
                    break

            t = self.consume()
            expr_tokens.append(t)

            if t.value == '(': paren_level += 1
            elif t.value == ')': paren_level -= 1
            elif t.value == '[': bracket_level += 1
            elif t.value == ']': bracket_level -= 1

            if paren_level < 0 or bracket_level < 0:
                raise ParserError("Unbalanced parentheses or brackets", t)

        if not expr_tokens:
             raise ParserError("Empty expression", self.peek())

        return Expression(expr_tokens)

    def parse_args(self):
        """Parses procedure call arguments."""
        self.consume() # (
        args = []
        if self.peek().value == ')':
            self.consume() # )
            return args

        while True:
            arg_expr = self.parse_expression([',', ')'])
            args.append(arg_expr)
            nxt = self.consume()
            if nxt.value == ')':
                break
            # nxt must be ','
        return args

    def parse_statement(self):
        """Parses a single statement (Assignment or ProcedureCall)."""
        # Skip labels
        while self.peek() and self.peek().type == 'NUMBER' and self.peek(1) and self.peek(1).value == ':':
            self.consume() # number
            self.consume() # :

        token = self.peek()
        if token is None: return None

        if token.type == 'ID':
            # Lookahead to distinguish assignment and call
            # We need to parse identifier first because of subscripts/dots
            start_pos = self.pos
            try:
                target = self.parse_identifier()
                nxt = self.peek()
                if nxt and nxt.type == 'ASSIGN':
                    self.consume('ASSIGN')
                    expr = self.parse_expression([';', 'END', 'ELSE', 'UNTIL'])
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
