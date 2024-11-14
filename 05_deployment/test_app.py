import requests

# Client data
client_data = {
    "job": "management",
    "duration": 400,
    "poutcome": "success"
}

# Make a POST request to the Flask app
response = requests.post('http://127.0.0.1:5000/predict', json=client_data)

# Print the prediction and probability
print(response.json())