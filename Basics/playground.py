str = "Hellol"

n = list(str)
print(n)
duplicate= []
for i in n:
    if i not in duplicate:
        duplicate.append(i)
    else:
        print(i)
index_obj = {}

for i in range(len(n)):
    print(n[i])
    if n[i] in index_obj:
        index_obj[n[i]+"t"] = i
    else:
        index_obj[n[i]] = i


print(index_obj)