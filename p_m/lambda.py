
a_list = [1, 2, 3, 4, 5, 6, 7, 8]

new_list = list(filter(lambda x: (x % 2 == 0), a_list))

print(new_list)
