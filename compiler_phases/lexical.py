class LexicalError(Exception):
    pass

def lex(code, lang):
    # Simple lexical analysis example
    if not code.strip():
        raise LexicalError("Empty code provided.")

    # Very basic tokenization by whitespace (demo only)
    tokens = code.replace('\n', ' \n ').split()
    # Check for illegal characters for C/C++/Python
    illegal_chars = ['$', '@', '#']  # example
    for i, token in enumerate(tokens):
        if any(c in token for c in illegal_chars):
            raise LexicalError(f"Illegal character '{token}' in code.")
    return tokens
