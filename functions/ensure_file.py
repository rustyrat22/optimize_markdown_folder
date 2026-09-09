import os


def ensure_file(folder_path: str, file_name: str) -> None:
    full_path = os.path.join(folder_path, file_name)
    if not os.path.exists(full_path):
        open(full_path, 'w').close()
