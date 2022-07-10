def binarySearch(list, x, low, high):
    while low <= high:
        mid = (low + high) // 2

        if list[mid] == x:
            return mid
        elif list[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
    return -1


a = [2,3,5,7,8]

#low = 0 && high = 5
#mid = 2 ---> 5
# bigger than mid index value mid + 1 == 7

# O(log n) --> it reduce the size of input in every step



print("index: ",binarySearch(a, 7, 0, len(a)-1))
