num = int(input("Enter a number: "))
flag = False

if num > 1:
    for x in range(2, num):
        if num % x == 0:
            flag = True
            break

if flag:
    print("Not Prime")
else:
    print("Prime")
