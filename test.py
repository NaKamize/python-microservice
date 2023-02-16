import requests

URL = "http://127.0.0.1:5000"

headers = {"Content-Type": "application/json; charset=utf-8"}


response = requests.post(
    URL + "/movies", headers=headers, json={'title': 'Indiana Jones', 'release_year': 1999})
print(response.json())

response = requests.post(
    URL + "/movies", headers=headers, json={'title': 'BatMan', 'description': 'Good movie', 'release_year': 2004})
print(response.json())

response = requests.put(
    URL + "/movies/1", headers=headers, json={'title': 'Indiana Jokes', 'description': 'Amazing movie', 'release_year': 2000})
print(response.json())

response = requests.get(URL + "/movies/1")
print(response.json())

response = requests.get(URL + "/movies")
print(response.json())
