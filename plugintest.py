from PIL import Image
from flask import Flask, request, jsonify
import pytesseract
import io
import base64

# Read the HTML file and extract the base64 string
with open('AIAssistant/VirtualAssistant/index2.html', 'r', encoding='utf-8') as file:
    html_content = file.read()

def download_blob_as_jpg(blob_url, file_name):
    # Step 1: Extract the base64 part from the 'data:image/jpeg;base64,...' URL
    if blob_url.startswith("data:image/jpeg;base64,"):
        base64_data = blob_url.split("data:image/jpeg;base64,")[1]
    elif blob_url.startswith("data:image/png;base64,"):
        base64_data = blob_url.split("data:image/png;base64,")[1]
    else:
        print("Unsupported image format.")
        return
    
    # Step 2: Decode the Base64 data into binary data
    image_data = base64.b64decode(base64_data)

    # Step 3: Save the decoded binary data to a file
    with open(file_name, "wb") as img_file:
        img_file.write(image_data)
    
    print(f"Image saved as {file_name}")

# Example usage
blob_url = html_content.data['image']
file_name = 'output_image.jpg'

download_blob_as_jpg(blob_url, file_name)
no_noise = "temp/no_noise.jpg"
img = Image.open(file_name)
ocr_result = pytesseract.image_to_string(img)
print(ocr_result)
