import os
import requests

url = "http://localhost:11434/v1/completions"
headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {os.getenv('OPENAI_API_KEY', '')}"
}
payload = {
    "model": "openhermes",
    "prompt": "What is 3 + 5?"
}

response = requests.post(url, headers=headers, json=payload)
print("Status Code:", response.status_code)
print("Response JSON:", response.json())
