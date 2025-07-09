import os
import subprocess


def run_python_file(working_directory, file_path):
    try:
        # Could maybe refactor others functions using this pattern
        working_path = os.path.abspath(working_directory)
        full_path = os.path.abspath(os.path.join(working_path, file_path))

        if not full_path.startswith(working_path):
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'

        if not os.path.exists(full_path):
            return f'Error: File "{file_path}" not found.'

        if not full_path.endswith(".py"):
            return f'Error: "{file_path}" is not a Python file.'

        result = subprocess.run(
            ["python3", file_path],
            capture_output=True,
            cwd=working_path,
            timeout=30,
            text=True,
        )

        output = []
        if result.stdout:
            output.append(f"STDOUT: {result.stdout}")
        if result.stderr:
            output.append(f"STDERR: {result.stderr}")
        if result.returncode != 0:
            output.append(f"Process exited with code {result.returncode}")
        if not output:
            return "No output produced"

        return "\n".join(output)
    except Exception as e:
        return f"Error: executing Python file: {e}"
