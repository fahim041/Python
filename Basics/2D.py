T = [[11, 12, 5, 2], [15, 6,10], [10, 8, 12, 5], [12,15,8,6]]

unique = []

res = list(set(i for j in T for i in j))

print(res) #unique
duplicate = []

for j in T:
    for i in j:
        if i not in unique:
            unique.append(i)
        else:
            print(i)
            duplicate.append(i)

print(duplicate)
unique.sort()
print(unique)