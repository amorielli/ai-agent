import os


def write_file(working_directory, file_path, content):
    try:
        working_path = os.path.abspath(working_directory)
        full_path = os.path.join(working_path, file_path)
        if not full_path.startswith(working_path):
            return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'

        if not os.path.exists(os.path.dirname(full_path)):
            os.makedirs(os.path.dirname(full_path))

        with open(full_path, "w") as f:
            f.write(content)

        return (
            f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
        )
    except Exception as e:
        return f"Error: {e}"
