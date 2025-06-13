from functools import wraps

import jwt
from flask import jsonify, request, current_app

from src.db import mysql


def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None

        if 'Authorization' in request.headers:
            token = request.headers['Authorization'].split(" ")[1]

        if not token:
            return jsonify({'message': 'Token is missing!'}), 401

        try:
            data = jwt.decode(token, current_app.config['SECRET_KEY'], algorithms=["HS256"])

            cur = mysql.connection.cursor()
            cur.execute("SELECT * FROM users WHERE email = %s AND jwt_token = %s", (data['email'], token))
            current_user = cur.fetchone()
            cur.close()

            if not current_user:
                return jsonify({'message': 'User not found!'}), 401

        except jwt.ExpiredSignatureError:
            return jsonify({'message': 'Token has expired!'}), 401
        except jwt.InvalidTokenError:
            return jsonify({'message': 'Invalid token!'}), 401

        combined_kwargs = {**data, **kwargs}
        return f(*args, **combined_kwargs)

    return decorated
