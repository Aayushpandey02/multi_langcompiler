
from flask import Flask, render_template, request, jsonify
import json
import os
print("TEMPLATE FOLDER:", os.path.abspath("template"))
print("FILES:", os.listdir("template"))

from datetime import datetime

from compiler_phases.lexical import lex
from compiler_phases.parser import parse
from compiler_phases.semantic import analyze_semantics
from compiler_phases.codegen import generate_code
from compiler_phases.runner import run_code
from compiler_phases.debugger import analyze_error
app = Flask(__name__, template_folder="template")

HISTORY_FILE = "history.json"
LANGUAGES = ['C', 'C++', 'Python']

# Load submission history or create empty
def load_history():
    if os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, "r") as f:
            return json.load(f)
    return []

def save_history(history):
    with open(HISTORY_FILE, "w") as f:
        json.dump(history, f, indent=2)

@app.route('/', methods=['GET', 'POST'])
def index():
    code = ''
    selected_lang = 'Python'
    phases = []
    output = ''
    error = ''
    suggestion = None
    history = load_history()

    if request.method == 'POST':
        code = request.form['code']
        stdin_input = request.form.get("stdin", "")
        selected_lang = request.form['language']

        try:
            # Compiler phases
            tokens = lex(code, selected_lang)
            phases.append(('Lexical Analysis', 'Passed'))

            ast = parse(tokens, selected_lang)
            phases.append(('Syntax Analysis', 'Passed'))

            analyze_semantics(ast, selected_lang)
            phases.append(('Semantic Analysis', 'Passed'))

            generated_code = generate_code(ast, selected_lang)
            phases.append(('Code Generation', 'Passed'))

            output = run_code(code, selected_lang, stdin_input)

        except Exception as e:
            error = str(e)
            # Automated debugging suggestion
            suggestion = analyze_error(error, code, selected_lang)

        # Save to history
        history.append({
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "language": selected_lang,
            "code": code,
            "output": output if not error else "",
            "error": error,
            "suggestion": suggestion['fixed_code'] if suggestion else None
        })
        save_history(history)

    return render_template('index.html',
                           languages=LANGUAGES,
                           selected_lang=selected_lang,
                           code=code,
                           phases=phases,
                           output=output,
                           error=error,
                           suggestion=suggestion,
                           history=history)

@app.route('/apply_suggestion', methods=['POST'])
def apply_suggestion():
    data = request.get_json()
    fixed_code = data.get('fixed_code', '')
    # Return fixed code to frontend to replace editor content
    return jsonify({'fixed_code': fixed_code})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
