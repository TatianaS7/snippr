from database import snippet_data, users
from snippet import f
import json, bcrypt
from bcrypt import hashpw, checkpw


next_id = 1

def seedDataToDB():
    global next_id

    with open("seedSnippets.json", "r") as s:
        data = json.load(s)
    for snippet in data:
        snippet_data[next_id] = {
            'id': next_id,
            'language': snippet['language'],
            'code': f.encrypt(snippet['code'].encode()).decode()
        }
        next_id += 1


user_id = 1

def seedUsers():
    global user_id

    with open("seedUsers.json", "r") as u:
        data = json.load(u)
    for user in data:
        hashedPassword = bcrypt.hashpw(user['password'].encode('utf-8'), bcrypt.gensalt())

        users[user_id] = {
            'id': user_id,
            'email': user['email'],
            'password': hashedPassword.decode('utf-8')
        }
        user_id += 1
