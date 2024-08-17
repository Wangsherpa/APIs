import pytesseract


async def read_image(image_path: str, lang: str = "eng"):
    try:
        text = pytesseract.image_to_string(image_path, lang=lang)
        return text
    except:
        return "[ERROR] Unable to process file: {0}".format(image_path)
