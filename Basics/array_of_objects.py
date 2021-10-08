arr = [
    {"id": 1, "name":"Jack", "age": 20},
    {"id": 2, "name":"Ryan", "age": 30},
    {"id": 3, "name":"Shadow", "age": 45}
]

arr =[x for x in arr if x['age'] != 30]
print(arr)