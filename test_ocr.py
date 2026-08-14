from utils.ocr import preprocess_image
import pytesseract
import cv2

img = cv2.imread("data/sample_images/test6.jpeg")
print("Image shape:", img.shape)

processed = preprocess_image("data/sample_images/test6.jpeg")
cv2.imwrite("data/sample_images/test6_processed.jpeg", processed)

text = pytesseract.image_to_string(processed, config='--psm 6')
print("OCR OUTPUT:")
print(text)