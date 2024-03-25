from flask import (Blueprint, request, jsonify, g)
from firebase_admin import auth

from backend.controllers.student import StudentController
from backend.controllers.teacher import TeacherController
from ..decorators.decorators import verify_token
from ..helpers.firebase_auth import authenticate_user_with_firebase

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/register', methods=["POST"])
@verify_token
def register():
    """ 
    Retrieves the user's information and sets the custom claims for the user.

    :return: The custom token with the custom claims attached to login in the client.
    """

    # Get the user's information from the request context stored by the verify_token decorator
    uid = g.uid
    accountType = request.json.get('accountType')
    institution_id = request.json.get('institution_id', None)

    # Set the user with the custom claims
    auth.set_custom_user_claims(uid, {'accountType': accountType})

    # Register the user uid in the database with the accountType
    if accountType == 'teacher':

        teacher_data = {
            'FIREBASE_UID': uid,
        }
        if institution_id is not None:
            teacher_data['INSTITUTION_ID'] = institution_id

        # Register the user in the OracleDB database
        TeacherController.create_teacher(teacher_data)

    elif accountType == 'student':

        student_data = {
            'FIREBASE_UID': uid,
        }
        if institution_id is not None:
            teacher_data['INSTITUTION_ID'] = institution_id
        StudentController.create_student(student_data)

    else:
        return jsonify({"error": "Invalid account type"}), 400

    # Generate a new access token with the custom claim attached
    custom_token = auth.create_custom_token(uid)

    # Decode the custom token to a string
    custom_token_str = custom_token.decode('utf-8')

    response_body = {
        "customToken": custom_token_str
    }

    return jsonify(response_body)

@auth_bp.route('/login', methods=['POST'])
def login():
    """
    Authenticate the user using email and password, then send a custom token to the client.

    return: The custom token with the custom claims attached to login in the client.
    """

    email = request.json.get('email')
    password = request.json.get('password')

    try:
        user_credentials = authenticate_user_with_firebase(email, password)
        id_token = user_credentials.get('idToken')

        if id_token is None:
            return jsonify({"error": "Invalid credentials"}), 400

        decoded_token = auth.verify_id_token(id_token)
        uid = decoded_token.get('uid')

        # Generate a new access token with the custom claim attached
        custom_token = auth.create_custom_token(uid)

        # Decode the custom token to a string
        custom_token_str = custom_token.decode('utf-8')

        return jsonify({"ok": True, "customToken": custom_token_str}), 200
    
    except Exception as e:
        return jsonify({"ok": False, "errorMessage": "Authentication failed"}), 500