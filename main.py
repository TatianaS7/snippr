from database import snippet_data
from snippet import f
import json

next_id = 1

def seedDataToDB():
    global next_id

    with open("seed_data.json", "r") as s:
        data = json.load(s)
    for snippet in data:
        snippet_data[next_id] = {
            'id': next_id,
            'language': snippet['language'],
            'code': f.encrypt(snippet['code'].encode()).decode()
        }
        next_id += 1
