import requests
import os
from dotenv import load_dotenv

load_dotenv()

BASE_URL = "https://carapi.app/api"
JWT = os.getenv("CARAPI_JWT")

HEADERS = {
    "Authorization": f"Bearer {JWT}",
    "Accept": "application/json"
}

def get_makes():
    url = f"{BASE_URL}/makes"
    response = requests.get(url, headers=HEADERS)
    try:
        data = response.json()
        return data.get("data", [])
    except Exception as e:
        print("❌ Failed to load makes:", e)
        return []

def get_models(make_id):
    print(f"Fetching models for make_id: {make_id}")
    url = (f"{BASE_URL}/models?json=["
           f"{{\"field\": \"make_id\", \"op\": \"=\", \"val\": {make_id}}},"
           f"{{\"field\": \"year\", \"op\": \">=\", \"val\": 2015}},"
           f"{{\"field\": \"year\", \"op\": \"<=\", \"val\": 2020}}]")

    response = requests.get(url, headers=HEADERS)
    try:
        data = response.json()
        return data.get("data", [])
    except Exception as e:
        print("❌ Failed to load models:", e)
        print("Response:", response.text)
        return []

def get_trims(model_id, year=None):
    url = f"{BASE_URL}/trims?model_id={model_id}"
    if year:
        url += f"&year={year}"
    response = requests.get(url, headers=HEADERS)
    try:
        data = response.json()
        return data.get("data", [])
    except:
        print("❌ Failed to load trims")
        return []

def get_trim_details(trim_id):
    url = f"{BASE_URL}/trims/{trim_id}"
    response = requests.get(url, headers=HEADERS)
    try:
        return response.json()
    except:
        print("❌ Failed to load trim details")
        return {}
