import re

def analyze_error(error_message, code, lang):
    """
   
                'suggestion': f"Add semicolon at line {line_num}",
                'fixed_code': "\n".join(fixed_lines)
            }

    # Example:rror',
            'line': None,
            'message': f"Undefined variable '{var_name}'. Consider declaring it before use.",
            'suggestion': f"Add declaration for variable '{var_name}' before usage.",
            'fixed_code': code }
