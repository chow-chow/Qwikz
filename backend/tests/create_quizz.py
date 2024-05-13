import requests

"""
    This script is used to test the creation of a quizz.
"""

url = "http://localhost:5000/quizz/create"

data = {
    "QUIZZ_CODE": "SND-IEP",
    "QUIZZ_NAME": "Examen Bebidos",
    "LIMIT_TIME": 60,
    "MAX_RETRY": 1,
    "QUESTIONS": [
        {
            "question": "¿Quién se robó mi queso?",
            "answers": [
                "El ratón",
                "Mis miedos",
                "Hola",
                "Adiós"
            ],
            "correctAnswer": 1,
            "file": {},
            "imageURL": "https://res.cloudinary.com/dsd9qmdge/image/upload/v1715471894/qwikz/owwcfhrkn1imtrnkwgzx.jpg"
        },
        {
            "question": "¿Qué es mejor?",
            "answers": [
                "AMD",
                "Intel",
                "NVIDIA",
                "Ryzon"
            ],
            "correctAnswer": 3,
            "file": {},
            "imageURL": "https://res.cloudinary.com/dsd9qmdge/image/upload/v1715471894/qwikz/cqm1rv42zu5ueikkd4lz.jpg"
        }
    ],
    "QWIKZGROUP_ID": 1
}

response = requests.post(url, json=data)
print(response)
