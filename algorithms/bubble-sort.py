def bubbleSort(arr):
    for i in range(len(arr)):
        swapped = False
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if swapped == False:
            break
    return arr

a = [5, 1, 4, 2, 8]

#first pass
#5,1,4,2,8 --> 1,5,4,2,8
#1,5,4,2,8 --> 1,4,5,2,8
#1,4,5,2,8 --> 1,4,2,5,8
#1,4,2,5,8 --> 1,4,2,5,8

#second pass
#1,4,2,5,8 --> 1,4,2,5,8
#1,4,2,5,8 --> 1,2,4,5,8
#1,2,4,5,8 --> 1,2,4,5,8
#1,2,4,5,8 --> 1,2,4,5,8


print(bubbleSort(a))
