a = [1, 2, 3, 4, 2, 4, 5, 9, 4]
b = []
for i in a:
    if i not in b:
        b.append(i)
        # print(b)
    else:
        pass
        print(i, end=" ")

print(b)
