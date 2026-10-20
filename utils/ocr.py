import cv2
import numpy as np
import pytesseract
from rapidfuzz import process, fuzz

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

KNOWN_MEDICINES = [
    "Ibuprofen", "Paracetamol", "Flexon", "Crocin",
    "Dolo 650", "Combiflam", "Azithromycin", "Cetirizine"
]

def preprocess_image(image_path):
    img = cv2.imread(image_path)
    if img is None:
        raise FileNotFoundError(f"Could not load image at: {image_path}")

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)

    thresh = cv2.adaptiveThreshold(
        blurred, 255,
        cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
        cv2.THRESH_BINARY,
        35, 11
    )

    kernel = np.ones((2, 2), np.uint8)
    closed = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)

    return closed


def extract_medicine_names(ocr_text, known_list=KNOWN_MEDICINES, threshold=70):
    words = ocr_text.split()
    found = {}

    for word in words:
        match, score, _ = process.extractOne(word, known_list, scorer=fuzz.ratio)
        if score >= threshold:
            if match not in found or score > found[match]:
                found[match] = score

    return found