FROM python:3.10-slim

# Upgrade pip and setuptools
RUN pip install --upgrade pip setuptools

# Install wget to download the TensorFlow Lite runtime
RUN apt-get update && apt-get install -y wget && rm -rf /var/lib/apt/lists/*

# Download the TensorFlow Lite runtime wheel file
RUN wget https://github.com/alexeygrigorev/tflite-aws-lambda/raw/main/tflite/tflite_runtime-2.14.0-cp310-cp310-linux_x86_64.whl

# Install additional libraries including the TensorFlow Lite runtime
RUN pip install pillow requests tensorflow==2.14.0 numpy>=1.23.5 flask  \
    tflite_runtime-2.14.0-cp310-cp310-linux_x86_64.whl

# Copy the lambda function code
COPY lambda_function.py .

# Set the CMD to the handler function
CMD ["python", "lambda_function.py"]
