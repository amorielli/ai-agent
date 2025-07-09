import os


def get_files_info(working_directory, directory=None):
    try:
        path = os.path.abspath(working_directory)
        working_directory_contents = os.listdir(path)
        working_directory_contents.append(".")
        if directory not in working_directory_contents:
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

        full_path = os.path.join(path, directory)
        if not os.path.isdir(full_path):
            return f'Error: "{directory}" is not a directory'

        directory_contents = os.listdir(full_path)
        files_info = []
        for entry in directory_contents:
            entry_path = os.path.join(full_path, entry)
            size = os.path.getsize(entry_path)
            is_dir = os.path.isdir(entry_path)
            files_info.append(f"- {entry}: file_size={size} bytes, is_dir={is_dir}")

        return "\n".join(files_info)
    except Exception as e:
        return f"Error: {e}"
