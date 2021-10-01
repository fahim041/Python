str = "World Hello"

print(str[0:2])

#iterating through string
count = 0
for letter in str:
    if(letter == "l"):
        count = count + 1

print(count)