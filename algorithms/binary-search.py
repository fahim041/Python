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


a = [2,3,5,6,8,22,44,53,73,81,90]
print("index: ",binarySearch(a, 81, 0, len(a)-1))
