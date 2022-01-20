import os
import requests
from datetime import *

NUTRITIONIX_API_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
NUTRITIONIX_APP_ID = os.environ.get("NUTRITIONIX_APP_ID")
NUTRITIONIX_API_KEY = os.environ.get("NUTRITIONIX_API_KEY")
SHEETY_ENDPOINT = "https://api.sheety.co/8191e27a182423e3999a53413bb663e5/workoutTracking/workouts"
SHEETY_API_KEY = os.environ.get("SHEETY_API_KEY")

nutritionix_auth_headers = {
    "x-app-id": NUTRITIONIX_APP_ID,
    "x-app-key": NUTRITIONIX_API_KEY,
}

sheety_auth_headers = {
    "Authorization": f"Bearer {SHEETY_API_KEY}",
    "Content-Type": "application/json"
}

query = {
    "query": input("What workouts did you do today? ")
}

response = requests.post(url=NUTRITIONIX_API_ENDPOINT, headers=nutritionix_auth_headers, json=query)
exercise_data = response.json()["exercises"]

for exercise in exercise_data:
    now = datetime.now()
    workout_data = {
        "workout": {
            "date": now.strftime("%x"),
            "time": now.strftime("%X"),
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    requests.post(url=SHEETY_ENDPOINT, headers=sheety_auth_headers, json=workout_data)
