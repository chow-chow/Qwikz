from flask import (Blueprint, request, jsonify, g)

from backend.controllers.student import StudentController
from backend.controllers.teacher import TeacherController
from ..decorators.decorators import verify_token
from firebase_admin import auth

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/register', methods=["POST"])
@verify_token
def register():
    """ 
    Retrieves the user's information and sets the custom claims for the user.

    :return: The user's information and the custom claims set.
    """

    # Get the user's information from the request context stored by the verify_token decorator
    uid = g.uid
    accountType = request.json.get('accountType')
    institution_id = request.json.get('institution_id', None)  # Es opcional

    # Set the user with the custom claims
    auth.set_custom_user_claims(uid, {'accountType': accountType})

    # Register the user uid in the database with the accountType
    if accountType == 'teacher':
        # Prepara los datos
        teacher_data = {
            'FIREBASE_UID': uid,
        }
        if institution_id is not None:
            teacher_data['institution_id'] = institution_id
        TeacherController.create_teacher(teacher_data)
    else:
        student_data = {
            'FIREBASE_UID': uid,
        }
        StudentController.create_student(student_data)

    # Generate a new access token with the custom claim attached
    custom_token = auth.create_custom_token(uid)

    # Decode the custom token to a string
    custom_token_str = custom_token.decode('utf-8')

    response_body = {
        "customToken": custom_token_str
    }

    return jsonify(response_body)

@auth_bp.route('/login', methods=['GET'])
def login():
  return 'Login route'