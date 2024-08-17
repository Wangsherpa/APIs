# OCR Text Extraction API

This repository contains a FastAPI-based web application that allows users to upload images and extract text from them using Optical Character Recognition (OCR). The OCR processing is powered by Tesseract.

## Features

- **File Upload**: Upload multiple image files for text extraction.
- **Asynchronous Processing**: Handles multiple OCR tasks concurrently to improve performance.
- **Tesseract Integration**: Leverages the Tesseract engine for accurate text extraction.
- **FastAPI**: Provides a fast and efficient REST API for easy integration with other applications.

## Project Structure
```bash
Tesseract
├── app
│   ├── __init__.py
│   ├── main.py
│   └── services
│       ├── __init__.py
│       ├── ocr.py
│       └── utils.py
└── requirements.txt
```


## Installation

### Prerequisites

- Python 3.8+
- Tesseract-OCR installed on your system. [Installation guide](https://github.com/tesseract-ocr/tesseract)

### Steps

1. **Clone the repository**:

   ```bash
   git clone https://github.com/Wangsherpa/APIs.git
   cd Tesseract-API
   ```
2. **Create and activate a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate
   ```
3. **Install the dependencies**:
   ```python
   pip install -r requirements.txt
   ```
4. **Install Tesseract**:
   Install Tesseract on your system. You can find installation instructions for various platforms [here](https://github.com/tesseract-ocr/tesseract).

## Running the Application
1. **Start the FastAPI server**:
   ```bash
   uvicorn app.main:app --reload
   ```
2. **Access the API**:
  - Open your browser and go to http://127.0.0.1:8000.
  - Visit the endpoint /api/v1/extract_text to upload images and perform OCR.
   

