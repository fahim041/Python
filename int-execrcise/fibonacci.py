def fibonacci(num):
    if num <= 1:
        return num
    else:
        return (fibonacci(num-1)+fibonacci(num-2))

nTerms = 10
for i in range(nTerms):
    print(fibonacci(i))