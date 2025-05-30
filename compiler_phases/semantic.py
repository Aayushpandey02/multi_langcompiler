class SemanticError(Exception):
    pass

def analyze_semantics(ast, lang):
    # Simple semantic check example: undefined variable check
    # For demo, if token 'undefined_var' present, error
    if 'undefined_var' in ast:
        raise SemanticError("Use of undefined variable 'undefined_var'")


