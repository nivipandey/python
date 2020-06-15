def decor(fun):
    def inner_fun():
        value=fun()
        return value+2
    return inner_fun
def num():
    return 30
result_fun=decor(num)
print(result_fun())
