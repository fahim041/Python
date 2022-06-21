def bubbleSort(arr):
    n = len(arr)
    
    for i in range(n -1):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                
    return arr
                
                
a = [4,3,5,6,74,667,8,2,3,5,7,8,22,45,66]
b = bubbleSort(a)

print(b)
