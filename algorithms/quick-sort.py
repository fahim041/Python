def quickSort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr.pop()

    items_greater = []
    items_lower = []

    for item in arr:
        if item > pivot:
            items_greater.append(item)
        else:
            items_lower.append(item)

    return quickSort(items_lower) + [pivot] + quickSort(items_greater)


a = [0,9,3,8,2,7,5]

#pivot = 5 --> n = 1
#list = 0, 3, 2, 5, 9, 8, 7
#left side ---> n = 2
#pivot = 2
#left list = 0,2,3

#right side
#pivot = 7 ---> n = 3
#right list = 7, 9, 8
#pivot = 8 ---> n = 4
#right list = 7, 8, 9

#full list = 0,2,3,5,7,8,9

print(quickSort(a))
