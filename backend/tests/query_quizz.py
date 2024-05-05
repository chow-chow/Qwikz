import requests

"""
    This script is used to test the query of all the quizzes assigned
    to a group.
"""

url = "http://localhost:5000/quizz/get_quizzes"

data = {
    "QWIKZGROUP_ID": 1
}

response = requests.post(url, json=data)

print(response.text)