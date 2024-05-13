import requests

"""
    This script is used to test the scoring of a quizz by updating the QUIZZ_APPLICATION_ID with the student's results.
"""

# URL del endpoint
url = "http://localhost:5000/quizz/score_quizz"

# Datos que se enviarán en la solicitud POST
data = {
    "QUIZZ_APPLICATION_ID": 44, 
    "RESULTS": 10
}

# Realizar la solicitud POST
response = requests.post(url, json=data)

# Imprimir la respuesta del servidor
print(response.text)