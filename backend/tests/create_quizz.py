import requests

"""
    This script is used to test the creation of a quizz.
"""

url = "http://localhost:5000/quizz/create"

data = {
    "QUIZZ_CODE": "A31-0X1",
    "QUIZZ_NAME": "QUIZZ_NAME",
    "LIMIT_TIME": 60,
    "MAX_RETRY": 1,
    "QUESTIONS": [
       ""
    ],
    "QWIKZGROUP_ID": 1
}

response = requests.post(url, json=data)

print(response)