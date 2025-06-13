import datetime
import hashlib

import jwt
from flask import Blueprint, jsonify, request, current_app

from .db import mysql
from .jwt import token_required

bp = Blueprint('auth', __name__, url_prefix='/auth')


@bp.route('/signup', methods=['POST'])
def signup():
    try:
        data = request.get_json()
        email = data.get('email')
        password = data.get('password')

        if not email or not password:
            return jsonify({"message": "All fields are required"}), 400

        hashed_password = hashlib.sha256(password.encode()).hexdigest()

        cursor = mysql.connection.cursor()
        cursor.execute('SELECT * FROM users WHERE email = %s', (email,))
        account = cursor.fetchone()

        if account:
            return jsonify({"message": "Account exists. Login instead"}), 409

        cursor.execute('INSERT INTO users (email, password) VALUES (%s, %s)', (email, hashed_password))
        token = jwt.encode({
            'email': email,
            'exp': datetime.datetime.now(tz=datetime.timezone.utc) + datetime.timedelta(days=30)
        }, current_app.config['SECRET_KEY'], algorithm="HS256")

        cursor.execute("UPDATE users SET jwt_token = %s WHERE email = %s", (token, email))
        mysql.connection.commit()
        cursor.close()

        return jsonify({"message": "User registered successfully", "token": token}), 201
    except Exception as e:
        return jsonify({"message": "Something went wrong"}), 500


@bp.route('/login', methods=['POST'])
def login():
    try:
        data = request.get_json()
        email = data.get('email')
        password = data.get('password')

        if not email or not password:
            return jsonify({"message": "All fields are required"}), 400

        hashed_password = hashlib.sha256(password.encode()).hexdigest()

        cursor = mysql.connection.cursor()
        cursor.execute('SELECT * FROM users WHERE email = %s', (email,))
        account = cursor.fetchone()

        if account and account[1] == hashed_password:  # account[1] is the password column
            token = jwt.encode({
                'email': email,
                'exp': datetime.datetime.now(tz=datetime.timezone.utc) + datetime.timedelta(days=30)
            }, current_app.config['SECRET_KEY'], algorithm="HS256")

            cursor.execute("UPDATE users SET jwt_token = %s WHERE email = %s", (token, email))
            mysql.connection.commit()
            cursor.close()
            return jsonify({"message": "Login successful", "token": token}), 200
        else:
            return jsonify({"message": "Invalid email or password"}), 401
    except Exception as e:
        return jsonify({"message": "Something went wrong"}), 500


@bp.route('/logout', methods=['POST'])
@token_required
def logout(**kwargs):
    email = kwargs.get('email')
    try:
        cursor = mysql.connection.cursor()
        cursor.execute('UPDATE users SET jwt_token = NULL WHERE email = %s', (email,))
        mysql.connection.commit()
        cursor.close()
        return jsonify({"message": "Logout successful"}), 200
    except Exception as e:
        return jsonify({"message": "Something went wrong"}), 500
