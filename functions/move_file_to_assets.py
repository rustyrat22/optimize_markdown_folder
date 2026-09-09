import os
import shutil

from .ensure_folder import ensure_folder

IMAGE_EXTENSIONS = {'.png', '.jpg', '.jpeg', '.gif', '.bmp', '.webp', '.svg', '.tiff', '.ico'}


def move_image_files_to_assets(article_file_path: str, image_paths: list[str]) -> list[str]:
    assets_folder = os.path.join(os.path.dirname(article_file_path), 'assets')
    ensure_folder(os.path.dirname(article_file_path), 'assets')
    moved_paths: list[str] = []
    for image_path in image_paths:
        if os.path.splitext(image_path)[1].lower() not in IMAGE_EXTENSIONS:
            continue
        destination = os.path.join(assets_folder, os.path.basename(image_path))
        shutil.move(image_path, destination)
        moved_paths.append(destination)
    return moved_paths