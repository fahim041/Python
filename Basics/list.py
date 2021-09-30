#slice
print("slice")
ex_list = [4,5,6,7,8,9,10]
print(ex_list[1:3])
print(ex_list[:])

#list are mutable
print("Mutable")
ex_list[1]= 33
print(ex_list)

#append and extend add items to the list --> last index
print("append")
ex_list.append(11)
print(ex_list)

#repeat
print("repeat")
new_list = [1,2,3,4]
print(new_list*3)

#insert
print("insert")
odd = [1,9]
odd.insert(1,3)
print(odd)

#del
print("delete")
del odd[1]
print(odd)

#remove
print("remove")
new_list_2 = [1,2,3,4,5,6]
new_list_2.remove(6)
print(new_list_2)
print("pop")
new_list_2.pop(1)
print(new_list_2)

#sort, reverse
print("index")
my_list = [3, 8, 1, 6, 0, 8, 4]
print(my_list[0])
print("sort")
my_list.sort()
print(my_list)
print("reverse")
my_list.reverse()
print(my_list)
