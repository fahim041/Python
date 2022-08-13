def smart_divide(func):
    def inner(a, b):
        if b == 0:
            print('error')
            return
        return func(a, b)
    return inner


@smart_divide
def divide(a, b):
    print(a/b)


divide(10, 2)
divide(10, 0)
