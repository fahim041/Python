def make_mutliplier(n):
    def multipiler_of(x):
        return x * n
    return  multipiler_of

times3 = make_mutliplier(3)
print(times3(4))