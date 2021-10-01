arr = [1,2,5,6]

missing_ele = []

for ele in range(arr[0], arr[-1]+1):
    if ele not in arr:
        missing_ele.append(ele)

print(missing_ele)