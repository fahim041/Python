str = "Hello world"
duplicate = []
for letter in str:
    if letter not in duplicate:
        duplicate.append(letter)
    else:
        print("Duplicate", letter)
print(duplicate)