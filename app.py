# Import Dependencies
from flask import Flask, request, jsonify
from database import snippet_data
from main import seedDataToDB


# Create instance of App
app = Flask(__name__)


# Runs Function to Seed Data
seedDataToDB()







if __name__ == '__main__':
    app.run(debug=True)
