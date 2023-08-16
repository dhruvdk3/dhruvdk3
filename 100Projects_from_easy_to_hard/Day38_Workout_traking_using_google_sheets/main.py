import requests, datetime, os

API_KEY = os.environ.get("API_KEY")
API_ID = os.environ.get("API_ID")
NUTRIT_ENDPOINT = os.environ.get("NUTRIT_ENDPOINT")
SHEETY_ENDPOINT = os.environ.get("SHEETY_ENDPOINT")
AUTHORIZATION = os.environ.get("AUTHORIZATION")
SHEETY_HEADER = {
    "Authorization": AUTHORIZATION
    }

exercise_parameters = {
    "query": input("What exercises you did? : ")
    }

headers = {
    "x-app-id": API_ID,
    "x-app-key": API_KEY,
    "Content-Type": "application/json"
    }

response = requests.post(url=NUTRIT_ENDPOINT, json=exercise_parameters, headers=headers)
nlp_data = response.json()["exercises"]

exercise = ", ".join([(i["user_input"]).title() for i in nlp_data])
duration = sum([float(i["duration_min"]) for i in nlp_data])
calories = sum([float(i["nf_calories"]) for i in nlp_data])

sheety_response = requests.get(url=SHEETY_ENDPOINT, headers=SHEETY_HEADER)
print(sheety_response.json())

sheety_data = {
    "workout": {
        "date": datetime.datetime.today().strftime("%d/%m/%y"),
        "time": datetime.datetime.now().strftime("%H:%M:%S"),
        "exercise": exercise,
        "duration": duration,
        "calories": calories,
    }
}


sheety_post = requests.post(
    url=SHEETY_ENDPOINT, json=sheety_data, headers=SHEETY_HEADER
)
print(sheety_post)
print(sheety_post.text)
