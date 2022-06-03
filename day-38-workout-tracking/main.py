import requests
from datetime import datetime

GENDER = "male"
WEIGHT_KG = "70"
HEIGHT_CM = "1.80"
AGE = "33"

APP_ID = "c5a2a919"
API_KEY = "efc1d1e40486a516e1fb29849545881f"

SHEETY_USERNAME = "your_sheety_username"
PASSWORD = "your_sheety_password"

nutritionix_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheety_endpoint = "https://api.sheety.co/a16b5433f2dc030c7bc505f07eef7979/day38MyWorkouts/workouts"

exercise_text = input("Tell me which exercises you did: ")

user_params = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE,
}
headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    "x-remote-user-id": "0",
}

response = requests.post(url=nutritionix_endpoint, json=user_params, headers=headers)
result = response.json()
print(result)

today = datetime.now()
today_formatted = today.strftime("%d/%m/%Y")
now_formatted = today.strftime("%X")

# Add data to google sheet

for exercise in result["exercises"]:
    sheet_inputs = {
            "workout": {
                "date": today_formatted,
                "time": now_formatted,
                "exercise": exercise["name"].title(),
                "duration": exercise["duration_min"],
                "calories": exercise["nf_calories"],
            }
    }

response3 = requests.post(url=sheety_endpoint, json=sheet_inputs, auth=(USERNAME, PASSWORD))
result3 = response3.json()
print(result3)
