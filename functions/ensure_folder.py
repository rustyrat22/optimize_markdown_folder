import os


def ensure_folder(folder_path: str, folder_name: str) -> None:
    full_path = os.path.join(folder_path, folder_name)
    if not os.path.exists(full_path):
        os.makedirs(full_path)
