import pytesseract


async def read_image(image_path: str, lang: str = "eng"):
    """
    Perform OCR on the given image file using Tesseract.

    Args:
        image_path (str): The path to the image file to be processed.
        lang (str, optional): The language to use for OCR. Defaults to "eng".

    Returns:
        str: The extracted text from the image, or an error message if processing fails.
    """

    try:
        text = pytesseract.image_to_string(image_path, lang=lang)
        return text
    except:
        return "[ERROR] Unable to process file: {0}".format(image_path)
