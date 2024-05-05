
from functools import wraps
from flask import (
    request, jsonify, g
)
from firebase_admin import auth

# Decorator to verify the token
def verify_token(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        # Get the token from the request header
        auth_header = request.headers.get('Authorization')
        if not auth_header:
            return jsonify({'message': 'Token is missing'}),  403

        # Extract the token by removing the 'Bearer ' prefix
        token = auth_header.split(' ')[1] if auth_header.startswith('Bearer ') else None
        if not token:
            return jsonify({'message': 'Invalid token format'}),  403

        # Verify the token and get the user's UID storing it in the request context
        try:
            decoded_token = auth.verify_id_token(token)
            uid = decoded_token['uid']
            
            # Store the uid and token in the request context
            g.uid = uid
            g.token = token
        except ValueError:
            return jsonify({'message': 'Token is invalid'}),  403

        return f(*args, **kwargs)

    return decorated_function

def verify_student_claim(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):

        auth_header = request.headers.get('Authorization')
        if not auth_header:
            return jsonify({'message': 'Token is missing'}),   403

        # Extract the token by removing the 'Bearer ' prefix
        token = auth_header.split(' ')[1] if auth_header.startswith('Bearer ') else None
        if not token:
            return jsonify({'message': 'Invalid token format'}),   403

        # Verify the token and get the user's UID storing it in the request context
        try:
            decoded_token = auth.verify_id_token(token)
            claims_match = decoded_token.get('accountType') == 'student'

            if claims_match is False:
                return jsonify({'message': 'User is not a student'}),   403

            uid = decoded_token['uid']

            # Store the uid and token in the request context
            g.uid = uid
            g.token = token

        except ValueError:
            return jsonify({'message': 'Token is invalid'}),   403

        return f(*args, **kwargs)

    return decorated_function


def verify_teacher_claim(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):

        auth_header = request.headers.get('Authorization')
        if not auth_header:
            return jsonify({'message': 'Token is missing'}),   403

        # Extract the token by removing the 'Bearer ' prefix
        token = auth_header.split(' ')[1] if auth_header.startswith('Bearer ') else None
        if not token:
            return jsonify({'message': 'Invalid token format'}),   403

        # Verify the token and get the user's UID storing it in the request context
        try:
            decoded_token = auth.verify_id_token(token)
            claims_match = decoded_token.get('accountType') == 'teacher'

            if claims_match is False:
                return jsonify({'message': 'User is not a teacher'}),   403

            uid = decoded_token['uid']
            
            # Store the uid and token in the request context
            g.uid = uid
            g.token = token

        except ValueError:
            return jsonify({'message': 'Token is invalid'}),   403

        return f(*args, **kwargs)

    return decorated_function