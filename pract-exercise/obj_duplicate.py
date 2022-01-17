b = [{'a': 7, 'b': 1}, {'a': 2, 'b': 2}, {'a': 7, 'b': 3}]

new = []
seen = set()

for i in b:
    key = (i['a'])
    if key in seen:
        print('duplicate', key)
        continue

    new.append(i)
    seen.add(key)

print('set', seen)
print('new list', new)
