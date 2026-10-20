from utils.ocr import preprocess_image, extract_medicine_names
from utils.speak import speak_medicines
import pytesseract
import cv2

img = cv2.imread("data/sample_images/test6.jpeg")
processed = preprocess_image("data/sample_images/test6.jpeg")
text = pytesseract.image_to_string(processed, config='--psm 6')

medicines = extract_medicine_names(text, threshold=70)
print("IDENTIFIED MEDICINES:", medicines)

speak_medicines(medicines)