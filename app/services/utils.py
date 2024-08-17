import os
import uuid
import shutil
from fastapi import UploadFile


def _save_file_to_server(
    uploaded_file: UploadFile, path: str = ".", save_as: str = None
) -> str:
    """
    Save an uploaded file to the server.

    Args:
        uploaded_file (UploadFile): The uploaded file to be saved.
        path (str, optional): The directory where the file will be saved. Defaults to the current directory (".").
        save_as (str, optional): The name to save the file as (without extension). Defaults to "default".

    Returns:
        str: The full path to the saved file.
    """

    if not save_as:
        save_as = str(
            uuid.uuid4()
        )  # Generates a unique name if `save_as` is not provided

    extension = os.path.splitext(uploaded_file.filename)[-1]
    temp_file = os.path.join(path, save_as + extension)
    try:
        os.makedirs(path, exist_ok=True)

        with open(temp_file, "wb") as buffer:
            shutil.copyfileobj(uploaded_file.file, buffer)
    except Exception as exc:
        raise IOError(f"Error saving file {uploaded_file.filename}: {exc}")

    return temp_file
