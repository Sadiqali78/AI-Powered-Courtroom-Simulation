import fitz  # PyMuPDF
import pytesseract
from PIL import Image
import io

def extract_text(uploaded_file):
    if uploaded_file.type == "application/pdf":
        doc = fitz.open(stream=uploaded_file.read(), filetype="pdf")
        text = ""
        for page in doc:
            text += page.get_text()
        return text.strip()
    elif uploaded_file.type.startswith("image/"):
        image = Image.open(uploaded_file).convert("RGB")
        return pytesseract.image_to_string(image)
    else:
        return uploaded_file.read().decode("utf-8")
