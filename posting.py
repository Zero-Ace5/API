import requests

URL = "https://jsonplaceholder.typicode.com/posts"

PAYLOAD = {
    "title": "I am still a noob",
    "body": "REAL BODY",
    "userID": 1
}

try:
    RESPONSE = requests.post(URL, json=PAYLOAD, timeout=1)
    print(RESPONSE.json())
except requests.exceptions.Timeout():
    print("The request timed out. Try again later")
