class SyntaxError(Exception):
    pass

def parse(tokens, lang):
    # Very basic parser: check for balanced brackets as a demo
    stack = []
    brackets = {'(': ')', '{': '}', '[': ']'}
    for token in tokens:
        if token in brackets.keys():
            stack.append(token)
        elif token in brackets.values():
            if not stack:
                raise SyntaxError(f"Unmatched closing bracket '{token}'")
            open_bracket = stack.pop()
            if brackets[open_bracket] != token:
                raise SyntaxError(f"Mismatched brackets '{open_bracket}' and '{token}'")
    if stack:
        raise SyntaxError(f"Unclosed bracket '{stack[-1]}'")
    # Return a dummy AST (just the token list here)
    return tokens

