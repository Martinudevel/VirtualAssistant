from PIL import Image
import pytesseract

img_file = "AIAssistant/VirtualAssistant/data/media-143132416195508600.jpg"
no_noise = "temp/no_noise.jpg"
img = Image.open(img_file)
ocr_result = pytesseract.image_to_string(img)
print(ocr_result)
