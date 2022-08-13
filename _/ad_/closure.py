def multiplier_of(n):
    def multiplier(x):
        return x * n
    return multiplier


times3 = multiplier_of(3)
times5 = multiplier_of(5)
print(times3(9))
print(times5(9))
