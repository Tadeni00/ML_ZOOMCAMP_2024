import tensorflow as tf
import os
from io import BytesIO
from urllib import request
from PIL import Image
import numpy as np

# Load the Keras model
model = tf.keras.models.load_model("model_2024_hairstyle.keras")

# Convert the model to TF-Lite format
converter = tf.lite.TFLiteConverter.from_keras_model(model)
tflite_model = converter.convert()

# Save the TF-Lite model
with open("model_2024_hairstyle.tflite", "wb") as f:
    f.write(tflite_model)

# Check the size of the TF-Lite model
file_size = os.path.getsize("model_2024_hairstyle.tflite")
print(f"Size of the converted TF-Lite model: {file_size / 1024000:.2f} MB")


# Load the TF-Lite model
interpreter = tf.lite.Interpreter(model_path="model_2024_hairstyle.tflite")
interpreter.allocate_tensors()

# Get model details
input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

# Print input and output details
print("Input details:", input_details)
print("Output details:", output_details)


def download_image(url):
    with request.urlopen(url) as resp:
        buffer = resp.read()
    stream = BytesIO(buffer)
    img = Image.open(stream)
    return img

def prepare_image(img, target_size):
    if img.mode != 'RGB':
        img = img.convert('RGB')
    img = img.resize(target_size, Image.NEAREST)
    return img

# Image URL
url = "https://habrastorage.org/webt/yf/_d/ok/yf_dokzqy3vcritme8ggnzqlvwa.jpeg"

# Download
image = download_image(url)

# Prepare the image
prepared_image = prepare_image(image, target_size=(200, 200))

# Convert the image to a numpy array
input_data = np.array(prepared_image, dtype=np.float32)

# Normalize the pixel values
input_data /= 255.0  # Normalize to [0, 1]

# Extract the first pixel's R channel
first_pixel_r_channel = input_data[0, 0, 0]  # Access row 0, column 0, R channel
print("Value of the first pixel's R channel:", f"{first_pixel_r_channel:.2f}")


input_data = np.expand_dims(input_data, axis=0)  # Add batch dimension


# Set the input tensor and invoke the interpreter
interpreter.set_tensor(input_details[0]['index'], input_data)
interpreter.invoke()

# Get the output tensor
output_data = interpreter.get_tensor(output_details[0]['index'])
print("Model output:", f"{float(output_data[0]):.3f}")

