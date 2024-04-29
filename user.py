from flask import Blueprint, request, jsonify
from bcrypt import hashpw, checkpw
from database import users
import json, bcrypt
import jwt, os

JWT_SECRET = os.getenv('JWT_SECRET')

user = Blueprint('user', __name__)


# Create a User
next_id = 1

@user.route('/', methods=['POST'])
def createUser():
    try:
        global next_id
        data = request.json

        if 'email' not in data or 'password' not in data:
            return jsonify({'error': 'Please provide an email and password'}), 400
        
        password = data['password']

        # Convert password into bytes then salt/hash it
        hashedPassword = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        
        # hashedPassword is decoded into a string to be serialized into JSON
        new_user = {
            'id': next_id,
            'email': data['email'],
            'password': hashedPassword.decode('utf-8')
        }
        # Add user to db with id
        users[next_id] = new_user
        print(users)

        # Increment ID for next entry
        next_id += 1

        # Generate token
        token = jwt.encode(new_user, JWT_SECRET)

        return jsonify({'success': token})
    except Exception as e:
        return jsonify({'error': str(e)}), 500


