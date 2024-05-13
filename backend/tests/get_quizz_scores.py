import requests

"""
    This script is used to test fetching quiz results for all students who took a specific quiz.
"""

url = "http://localhost:5000/quizz/get_quizz_results"

data = {
    "QUIZZ_ID": 25
}

response = requests.post(url, json=data)

print(response.text)