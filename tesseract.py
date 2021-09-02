from PIL import Image
import pytesseract

pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'
lol=pytesseract.image_to_string(Image.open('C:/Users/iball/Desktop/DrawingSoftware/pdfsoftware/docs/teseract/handwritten2.jpg'))
print(lol)