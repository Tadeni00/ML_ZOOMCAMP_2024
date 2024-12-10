import requests

# Assuming your server is running locally on port 8000
url = "http://localhost:8000/"  # Use the root URL for your local server

# Correctly structure the data as a dictionary
data = {'image_url': 'https://habrastorage.org/webt/yf/_d/ok/yf_dokzqy3vcritme8ggnzqlvwa.jpeg'}

# Send a POST request with the correct data structure
result = requests.post(url, json=data)

# Print the result; it should be JSON format
print(result.json())
