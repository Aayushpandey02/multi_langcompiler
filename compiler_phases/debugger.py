import re

def analyze_error(error_message, code, lang):
    """
    Analyze the error message and source code,
    then return a suggestion dict:
    {
        'error_type': 'SyntaxError',
        'line': 5,
        'message': 'Missing semicolon',
        'suggestion': 'Add a semicolon at line 5',
        'fixed_code': 'corrected code snippet'
    }
    """

    # Basic patterns for demo:
    # Missing semicolon (C/C++)
    missing_semicolon_pattern = re.compile(r"expected ';'")

    # Undefined variable (semantic)
    undefined_var_pattern = re.compile(r"undefined variable '(\w+)'")

    # Indentation error (Python)
    indent_error_pattern = re.compile(r"IndentationError")

    lines = code.split('\n')

    # Default no suggestion
    suggestion = None

    # Example: Missing semicolon fix
    if lang in ['C', 'C++'] and missing_semicolon_pattern.search(error_message):
        # Heuristic: Add ';' to line before error
        line_num = find_error_line(error_message, code) or 0
        if 0 <= line_num-1 < len(lines):
            fixed_line = lines[line_num-1].rstrip() + ';'
            fixed_lines = lines[:line_num-1] + [fixed_line] + lines[line_num:]
            suggestion = {
                'error_type': 'SyntaxError',
                'line': line_num,
                'message': "Missing semicolon detected.",
                'suggestion': f"Add semicolon at line {line_num}",
                'fixed_code': "\n".join(fixed_lines)
            }

    # Example: Undefined variable
    elif undefined_var_pattern.search(error_message):
        match = undefined_var_pattern.search(error_message)
        var_name = match.group(1)
        suggestion = {
            'error_type': 'SemanticError',
            'line': None,
            'message': f"Undefined variable '{var_name}'. Consider declaring it before use.",
            'suggestion': f"Add declaration for variable '{var_name}' before usage.",
            'fixed_code': code }
