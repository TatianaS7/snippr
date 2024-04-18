from seed_data import seed_snippets
from database import snippet_data

next_id = 1

def seedDataToDB():
    global next_id
    for snippet in seed_snippets:
        snippet_data[next_id] = {
            'language': snippet['language'],
            'code': snippet['code']
        }
        next_id += 1