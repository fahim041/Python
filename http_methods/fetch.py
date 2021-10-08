import requests

r = requests.get("https://jsonplaceholder.typicode.com/posts")

content = r.json()
print(content)
id = (x for x in content if x["id"]==2)
print(list(id))

title_list = list(filter(lambda x: x["id"] == 1, content))

print(title_list)