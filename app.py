# Import Dependencies
from flask import Flask, request, jsonify
from database import snippet_data
from main import seedDataToDB


# Create instance of App
app = Flask(__name__)


# Runs Function to Seed Data
seedDataToDB()


# ROUTES

# Get All Snippets
@app.route('/snippet', methods=['GET'])
def getAllSnippets():
    try:
        return jsonify(snippet_data)
    except Exception as e:
        return jsonify({'error': str(e)}), 500





if __name__ == '__main__':
    app.run(debug=True)
