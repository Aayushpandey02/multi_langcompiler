class CodegenError(Exception):
    pass

def generate_code(ast, lang):
    # Return code as string for runner
    # For Python: just join tokens
    # For C/C++: join tokens (placeholder)
    if lang in ['C', 'C++', 'Python']:
        return " ".join(ast)
    else:
        raise CodegenError("Unsupported language for code generation")

