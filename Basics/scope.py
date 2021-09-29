def outer_function():
    b = 20
    def inner_func():
        c = 30
        print(a)
        print(b)
    inner_func()


a = 10
outer_function()
