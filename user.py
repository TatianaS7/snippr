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


# Login
@user.route('/login', methods=['POST'])
def login():
    email = request.json.get('email')
    password = request.json.get('password')

    if not email or not password:
        return jsonify({'error': 'Please provide an email and password'}), 400
        
    userID = None
    for user_id, user_info in users.items():
        if user_info['email'] == email:
            userID = user_id
            break

    if userID is None:
        return jsonify({'error': 'User not found'}), 401

    hashedPassword = users[userID]['password'].encode('utf-8')

    if not bcrypt.checkpw(password.encode('utf-8'), hashedPassword):
        return jsonify({'error': 'Incorrect Password'}), 401
    else:
        token = jwt.encode({'email': email, 'password': password }, JWT_SECRET)
        return jsonify({'success': token})


# Get a User
@user.route('/', methods=['GET'])
def getUser():
    email = request.json.get('email')
    password = request.json.get('password')

    if not email or not password:
        return jsonify({'error': 'Email and password required'}), 400

    userID = None
    for user_id, user_info in users.items():
        if user_info['email'] == email:
            userID = user_id
            break

    if userID is None:
        return jsonify({'error': 'User not found'}), 401

    hashedPassword = users[userID]['password'].encode('utf-8')

    if not bcrypt.checkpw(password.encode('utf-8'), hashedPassword):
        return jsonify({'error': 'Incorrect Password'}), 401
    else:
        return jsonify({'id': user_info['id'],'email': user_info['email']})

