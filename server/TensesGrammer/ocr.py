import cv2
import numpy as np
import pytesseract as tess
tess.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def image_to_text(image):
    image=cv2.imread(image,0)
    kernel = np.ones((1,1),np.uint8)
    opening=cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)
    text = tess.image_to_string(opening,lang='eng')
    return (text)

