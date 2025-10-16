import requests

URL = "https://jsonplaceholder.typicode.com/posts"

PAYLOAD = {
    "title": "I am still a noob",
    "body": "REAL BODY",
    "userID": 1
}

RESPONSE = requests.post(URL, json=PAYLOAD)
print(RESPONSE.json())
