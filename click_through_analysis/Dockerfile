# Start with a base Python image
FROM python:3.12.1-slim

# Set a working directory in the container
WORKDIR /app

# Install system dependencies for compiling Python packages
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# Copy only requirements.txt first to leverage Docker caching
COPY requirements.txt .

# Install dependencies from requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy all application files into the container
COPY . .

RUN useradd -ms /bin/bash nonroot
USER nonroot

EXPOSE 5000

# The command to run the application
CMD ["python", "app.py"]
