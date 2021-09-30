double = lambda x : x * 2

print(double(5))

#filter
my_list = [1,5,4,6,3,5,11,10, 10]

new_list = list(filter(lambda x: (x % 2 == 0), my_list))

print(new_list)

#map
my_list_2 = [1,4,5,4,5,6,7]
new_list_2 = list(filter(lambda x: x * 2, my_list_2))

print(new_list_2)