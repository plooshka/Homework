a = "I am global variable!"


def enclosing_funcion():
    a = "I am variable from enclosed function!"

    def inner_function():
        # a = "I am local variable!"
        # global a
        nonlocal a
        print(a)

    return inner_function


inner_function = enclosing_funcion()
inner_function()
