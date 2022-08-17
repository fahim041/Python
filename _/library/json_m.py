import json

movies = [
    {"id":1, "title":"Rock", "year":1989},
    {"id":2, "title":"Cop", "year":2000}
]

data = json.dumps(movies)

parse = json.loads(data)
for p in parse:
    print(p['title'])