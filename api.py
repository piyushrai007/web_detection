from flask import Flask, request, jsonify
from flask_cors import CORS
from ultralytics import YOLO
from PIL import Image
import numpy as np
import io
import requests
import base64

from flask import Flask

api = Flask(__name__)

# Define routes and other Flask configurations here

CORS(api)

# Load a pretrained YOLOv8 model
model = YOLO('best.pt') # pretrained YOLOv8n model

def process_image(image):
    # Run inference
    results = model(image, conf=0.09999999999999999)

    # Process results
    for r in results:
        im_array = r.plot()  # plot a BGR numpy array of predictions
        im = Image.fromarray(im_array[..., ::-1])  # RGB PIL image

    # Convert image to base64-encoded string
    buffered = io.BytesIO()
    im.save(buffered, format="JPEG")
    img_str = base64.b64encode(buffered.getvalue()).decode()

    return img_str

def process_url_image(url):
    response = requests.get(url)
    if response.status_code == 200:
        img = Image.open(io.BytesIO(response.content))
        return process_image(img)
    else:
        return None

@api.route('/detect', methods=['POST'])
def detect_objects():
    if 'file' in request.files:
        # File upload scenario
        file = request.files['file']
        img_bytes = file.read()
        img = Image.open(io.BytesIO(img_bytes))
        detections = process_image(img)
        return jsonify({'image': detections})

    elif 'url' in request.form:
        # URL scenario
        url = request.form['url']
        if url.startswith('https://www.figma.com/file/'):
            # Figma page URL
            # Handle Figma page URLs
            return jsonify({'error': 'Figma page URL handling not implemented yet'})
        else:
            # Other image URL
            detections = process_url_image(url)
            if detections:
                return jsonify({'image': detections})
            else:
                return jsonify({'error': 'Failed to process image from URL'})

    else:
        return jsonify({'error': 'No file or URL provided'})

if __name__ == '__main__':
    api.run(debug=True)
