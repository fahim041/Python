a = {"value": 20}

b = a

print(a)  # {'value':20}
print(b)  # {'value':20}

a["value"] = 35

print(a)  # {'value':35}
print(b)  # {'value':35}
