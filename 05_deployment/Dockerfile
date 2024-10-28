# Start with the base image
FROM svizor/zoomcamp-model:3.11.5-slim

# Set the working directory
WORKDIR /app

# Install pipenv if not included in the base image
RUN pip install pipenv flask scikit-learn gunicorn

# Copy the Pipfile and Pipfile.lock
COPY Pipfile Pipfile.lock ./ 

# Install dependencies
RUN pipenv install --deploy --ignore-pipfile

# Copy your Flask app script
COPY app.py ./ 

# Run your application with Gunicorn
CMD gunicorn -b 0.0.0.0:5000 app:app


