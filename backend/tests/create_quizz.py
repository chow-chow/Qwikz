import requests

"""
    This script is used to test the creation of a quizz.
"""

url = "http://localhost:5000/quizz/create"

data = {
    "QUIZZ_CODE": "A31-0X1",
    "QUIZZ_NAME": "QUIZZ_NAME_2_Test",
    "LIMIT_TIME": 60,
    "MAX_RETRY": 1,
    "QUESTIONS": [
        {
            "id": 1,
            "question": "¿Qué coño inició la Primera Guerra Mundial?",
            "correct_answer": "El asesinato del Archiduque Franz Ferdinand de Austria",
            "incorrect_answers": [
                "El hundimiento del Titanic",
                "La invasión de Polonia por Alemania",
                "La Revolución Francesa"
            ]
        },
        {
            "id": 2,
            "question": '¿Quién es el autor de "Cien años de soledad"?',
            "correct_answer": "Gabriel García Márquez",
            "incorrect_answers": [
                "Julio Cortázar",
                "Mario Vargas Llosa",
                "Pablo Neruda"
            ]
        },
        {
            "id": 3,
            "question": "¿En qué deporte se utiliza un disco?",
            "correct_answer": "Hockey sobre hielo",
            "incorrect_answers": ["Fútbol", "Baloncesto", "Béisbol"]
        },
        {
            "id": 4,
            "question": "¿Qué sustancia es conocida como la 'molécula de la vida'?",
            "correct_answer": "El ADN",
            "incorrect_answers": ["La glucosa", "La insulina", "La proteína"]
        }
    ],
    "QWIKZGROUP_ID": 1
}

response = requests.post(url, json=data)
print(response)
