from flask import Blueprint, request, jsonify
from database import snippet_data

snippet = Blueprint('snippet', __name__)


# ROUTES
next_id = 9

# Get All Snippets
@snippet.route('/all', methods=['GET'])
def getAllSnippets():
    try:
        return jsonify(snippet_data)
    except Exception as e:
        return jsonify({'error': str(e)}), 500


# Get a Snippet (by id)
@snippet.route('/<id>', methods=['GET'])
def getSnippet(id):
    try:
        snippet = snippet_data[int(id)]
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
        
        new_snippet = {
            'language': data['language'], 
            'code': data['code']
        }
        snippet_data[next_id] = new_snippet
        next_id += 1
        return jsonify(new_snippet), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

