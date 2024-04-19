from seed_data import seed_snippets
from database import snippet_data
from snippet import Fernet, f

next_id = 1

def seedDataToDB():
    global next_id
    for snippet in seed_snippets:
        snippet_data[next_id] = {
            'language': snippet['language'],
            'code': f.encrypt(snippet['code'].encode()).decode()
        }
        next_id += 1