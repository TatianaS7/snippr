# Import Dependencies
from flask import Flask, request, jsonify
from database import snippet_data
from main import seedDataToDB


# Create instance of App
app = Flask(__name__)


# Runs Function to Seed Data
seedDataToDB()



# ROUTES
next_id = 9

# Get All Snippets
@app.route('/snippet', methods=['GET'])
def getAllSnippets():
    try:
        return jsonify(snippet_data)
    except Exception as e:
        return jsonify({'error': str(e)}), 500


# Get a Snippet (by id)
@app.route('/snippet/<id>', methods=['GET'])
def getSnippet(id):
    try:
        snippet = snippet_data[int(id)]
        return jsonify(snippet)
    except Exception as e:
        return jsonify({'error': str(e)}), 500


# Create a Snippet
@app.route('/snippet', methods=['POST'])
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




if __name__ == '__main__':
    app.run(debug=True)
