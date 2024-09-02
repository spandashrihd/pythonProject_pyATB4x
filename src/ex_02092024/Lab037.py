#inner function can access local variable of outer function

def outer_function():
    var=90

    def inner_function():
        print(var)

    def inner_function2():
        print(var)

    inner_function()
    inner_function2()

outer_function()