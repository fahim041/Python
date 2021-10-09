items = [
    ('product1', 10),
    ('product2', 7),
    ('product3', 15)
]

items.sort(key=lambda item: item[1])
print(items)
