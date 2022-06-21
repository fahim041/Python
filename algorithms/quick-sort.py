def quickSort(arr):
    n = len(arr)
    if n <= 1:
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

    
a = [4,3,5,6,74,667,8,2,3,5,7,8,22,45,66]

print(quickSort(a))