arr = [
    {"id": 1, "name": "Jack", "age": 20},
    {"id": 2, "name": "Ryan", "age": 30},
    {"id": 3, "name": "Shadow", "age": 45}
]

arr =[x for x in arr if x['age'] > 25]
print(arr)

new_list = list(filter(lambda x : x["age"] > 25, arr))
print(new_list)

