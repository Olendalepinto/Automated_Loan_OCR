import pytesseract
from PIL import Image

# pytesseract.pytesseract.tesseract_cmd = r'E:\\ocr\\tesseract.exe'

def extract_text(image):
    return pytesseract.image_to_string(image)
