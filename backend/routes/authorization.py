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

@auth_bp.route('/verify', methods=['POST'])
@verify_token
def verify():
    """
    Using Firebase SDK verifies the custom claims of the user declared in the token.

    return: A boolean value indicating if the user has the custom claim or not.
    """

    # Get the user's information from the request context stored by the verify_token decorator
    token = g.token
    accountType = request.json.get('accountType')

    # Get the user's custom claims
    custom_claims = auth.verify_id_token(token)

    print("This user has the following custom claims: ", custom_claims.get('accountType'))

    # Check if the server and client custom claims match
    claims_match = custom_claims.get('accountType') == accountType

    if claims_match is False:
        return jsonify({"error": "The custom claims declared in the client do not match"}), 400
    else:
        return jsonify({"ok": claims_match})