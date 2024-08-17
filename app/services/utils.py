import os
import shutil
from fastapi import UploadFile


def _save_file_to_server(
    uploaded_file: UploadFile, path: str = ".", save_as: str = "default"
) -> str:
    extension = os.path.splitext(uploaded_file.filename)[-1]
    temp_file = os.path.join(path, save_as + extension)

    with open(temp_file, "wb") as buffer:
        shutil.copyfileobj(uploaded_file.file, buffer)

    return temp_file
