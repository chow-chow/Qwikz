import requests

"""
    This script is used to test the query of a quizz to send it to a student.
"""

url = "http://localhost:5000/quizz/get_student_quizz"

data = {
    "QWIKZGROUP_ID": 1
}

response = requests.post(url, json=data)

print(response.text)