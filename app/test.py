import requests

# Example JSON data with numeric feature values
data = {
    "feature1": 10.0,
    "feature2": 20.0,
    "feature3": 30.0,
    # Add more feature-value pairs as needed
}

# Send POST request to Flask endpoint
response = requests.post('http://127.0.0.1:5000/predict', json=data)

# Print response
print(response.json())
