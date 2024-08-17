
import time
import asyncio
from fastapi import FastAPI, File, UploadFile
from typing import List

from app.services import utils
from app.services import ocr


app = FastAPI()


@app.get("/")
def root():
    return {"message": "Visit the endpoint: /api/v1/extract_text to perform OCR."}


@app.post("/api/v1/extract_text")
async def extract_text(Images: List[UploadFile] = File(...)):
    response = {}
    s = time.time()
    tasks = []
    for img in Images:
        print("Images Uploaded: ", img.filename)
        temp_file = utils._save_file_to_server(img, path="./", save_as=img.filename)
        tasks.append(asyncio.create_task(ocr.read_image(temp_file)))

    texts = await asyncio.gather(*tasks)
    for i in range(len(texts)):
        response[Images[i].filename] = texts[i]
    response["Time Taken"] = round((time.time() - s), 2)
    return response
