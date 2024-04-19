from flask import Blueprint, request, jsonify
from database import snippet_data
from cryptography.fernet import Fernet
import os


f = Fernet(os.getenv('ENCRYPTION_KEY', 'none'))

snippet = Blueprint('snippet', __name__)


# ROUTES
next_id = 9

# Get All Snippets
@snippet.route('/all', methods=['GET'])
def getAllSnippets():
    try:
        # Figure out how to decrypt without reassigning the code value completely. 
        # This is whats causing an error when you switch between getting all snippets and getting a specific snippet by id  

        # for id in snippet_data:
        #     snippet = snippet_data[id]

        #     decrypted_code = f.decrypt(snippet['code']).decode()
        #     snippet['code'] = decrypted_code

        return jsonify(snippet_data)
    except Exception as e:
        return jsonify({'error': str(e)}), 500


# Get a Snippet (by id)
@snippet.route('/<int:id>', methods=['GET'])
def getSnippet(id):
    try:
        snippet = snippet_data[id]
        
        decrypted_code = f.decrypt(snippet['code']).decode()
        snippet['code'] = decrypted_code

        return jsonify(snippet)
    except Exception as e:
        return jsonify({'error': str(e)}), 500


# Create a Snippet
@snippet.route('/', methods=['POST'])
def createSnippet():
    try:
        global next_id
        data = request.json

        if 'language' not in data or 'code' not in data:
            return jsonify({'error': 'Missing language or code'}), 400
        
        encrypted_code = f.encrypt(data['code'].encode())

        new_snippet = {
            'id': next_id,
            'language': data['language'], 
            'code': encrypted_code.decode()
        }
        snippet_data[next_id] = new_snippet
        next_id += 1
        return jsonify(new_snippet), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

