str = "Hello world I am not going to sleep Hello again sleep sleep"

print(str)
x = str.split()
print(x)
unique_word = []
obj = {}
for word in x:
    if word not in unique_word:
        unique_word.append(word)
    else:
        if word in obj:
            obj[word] = obj[word] + 1
        else:
            obj[word] = 2

print(obj)