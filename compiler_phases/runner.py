import subprocess
import tempfile
import os

class RuntimeError(Exception):
    pass

def run_code(code, lang, stdin_input=""):
    with tempfile.NamedTemporaryFile(delete=False, suffix={
        'C': '.c', 'C++': '.cpp', 'Python': '.py'
    }[lang]) as tmp:
        tmp.write(code.encode())
        tmp.flush()
        filename = tmp.

    try:
        if lang in ['C', 'C++']:
            exe_file = filename + '.out'
            compiler = 'gcc' if lang == 'C' else 'g++'
            result = subprocess.run([compiler, filename, '-o', exe_file], capture_output=True, text=True)
            if result.returncode != 0:
                raise RuntimeError(f"Compilation failed:\n{result.stderr}")
            run_result = subprocess.run(
    [exe_file],
    input=stdin_input,
    capture_output=True,
    text=True,
    timeout=10
)
            if run_result.returncode != 0:
                raise RuntimeError(f"Runtime error:\n{run_result.stderr}")
            output = run_result.stdout
        else:
            run_result = subprocess.run(
    ['python', filename],
    input=stdin_input,
    capture_output=True,
    text=True,
    timeout=10
)
            if run_result.returncode != 0:
                raise RuntimeError(f"Runtime error:\n{run_result.stderr}")
            output = run_result.stdout
        return output
    finally:
        os.remove(filename)
        if lang in ['C', 'C++'] and os.path.exists(exe_file):
            os.remove(exe_file)
