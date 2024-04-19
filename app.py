# Import Dependencies
from flask import Flask
from main import seedDataToDB
from user import user
from snippet import snippet
from dotenv import find_dotenv, load_dotenv

ENV_FILE = find_dotenv()
if ENV_FILE:
    load_dotenv(ENV_FILE)


# Create instance of App
app = Flask(__name__)


# Runs Function to Seed Data
seedDataToDB()


# Routes
app.register_blueprint(user, url_prefix="/users")
app.register_blueprint(snippet, url_prefix="/snippet")






if __name__ == '__main__':
    app.run(debug=True)
