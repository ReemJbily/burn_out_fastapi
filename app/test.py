import requests

api_endpoint = "http://0.0.0.0:8080/predict/"

payload = {
    "Gender": 5.1,
    "Company_Type": 3.5,
    "Remote": 3.4,
    "Designation": 1.2
    "Resource": 1.2
    }

headers = {
    "accept": "application/json",
    "Content-Type": "application/json"
    }

response = requests.post(api_endpoint, headers=headers, json=payload)

print(response.json())