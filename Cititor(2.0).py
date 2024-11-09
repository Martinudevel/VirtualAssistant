
from flask import Flask, request, jsonify
import base64
import keras_ocr
import os
import io
from flask_cors import CORS
import numpy as np
from PIL import Image

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route('/scan', methods=['POST'])
def scan():
    try:
        # Get the uploaded file
        if 'file' not in request.files:
            return jsonify({"error": "No file part"}), 400

        file = request.files['file']
        if file.filename == '':
            return jsonify({"error": "No selected file"}), 400
        
        image = Image.open(io.BytesIO(blob_data))  # blob_data should be a byte stream
        
        print("Processing file:", file.filename)
        # Process the file using keras_ocr
        pipeline = keras_ocr.pipeline.Pipeline()
        image = keras_ocr.tools.read(file_stream)
        prediction_groups = pipeline.recognize([image])

        print(prediction_groups[0])

        # Return the predictions as a JSON response
        return jsonify(prediction_groups[0])
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)