from flask import Flask, request, jsonify
import numpy as np
from PIL import Image
from io import BytesIO
import requests
import tensorflow as tf

app = Flask(__name__)

def download_image(url):
    response = requests.get(url)
    img = Image.open(BytesIO(response.content))
    return img

def prepare_image(img, target_size=(200, 200)):
    if img.mode != 'RGB':
        img = img.convert('RGB')
    img = img.resize(target_size)
    img_array = np.array(img, dtype=np.float32)
    img_array /= 255.0  # Normalize pixel values
    img_array = np.expand_dims(img_array, axis=0)  # Add batch dimension
    return img_array

@app.route('/', methods=['POST'])
def predict():
    data = request.get_json()
    image_url = data.get('image_url')
    img = download_image(image_url)
    input_data = prepare_image(img)

    interpreter = tf.lite.Interpreter(model_path="model_2024_hairstyle_v2.tflite")
    interpreter.allocate_tensors()

    input_details = interpreter.get_input_details()
    output_details = interpreter.get_output_details()

    interpreter.set_tensor(input_details[0]['index'], input_data)
    interpreter.invoke()

    output_data = interpreter.get_tensor(output_details[0]['index'])
    score = output_data[0][0]

    return jsonify({'score': score})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
