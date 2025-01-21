# Use the official Python image
FROM python:3.12-slim

# Set the working directory
WORKDIR /app

# Copy the data folder into the container
COPY ./data ./data

# Copy the requirements file
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Download SpaCy model
RUN python -m spacy download en_core_web_md

# Copy the application code
COPY ./src ./src
COPY app.py .

# Expose Streamlit's default port
EXPOSE 8501

# Run the Streamlit app
CMD ["streamlit", "run", "app.py", "--server.address", "0.0.0.0", "--server.port", "8501"]
