from flask import Blueprint, request, jsonify
from bcrypt import hashpw, checkpw
from database import users
import json, bcrypt

user = Blueprint('user', __name__)

# Create a User
@user.route('/', methods=['POST'])
def createUser():
    try:
        data = request.json

        if 'email' not in data or 'password' not in data:
            return jsonify({'error': 'Please provide an email and password'}), 400
        
        password = data['password']

        # Convert password into bytes then salt/hash it
        hashedPassword = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        
        # hashedPassword is decoded into a string to be serialized into JSON
        new_user = {
            'email': data['email'],
            'password': hashedPassword.decode('utf-8')
        }
        return jsonify(new_user)
    except Exception as e:
        return jsonify({'error': str(e)}), 500
