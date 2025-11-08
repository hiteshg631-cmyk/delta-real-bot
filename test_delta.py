import requests
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

API_KEY = os.getenv("DELTA_API_KEY")
API_SECRET = os.getenv("DELTA_API_SECRET")

url = "https://api.delta.exchange/v2/products"

headers = {
    "api-key": API_KEY,
    "api-secret": API_SECRET
}

response = requests.get(url, headers=headers)

print("Status Code:", response.status_code)
print("Response:", response.text[:500])  # सिर्फ पहले 500 characters दिखाने के लिए
