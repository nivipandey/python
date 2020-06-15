a=10
def f():
    a=20
    x=globals()["a"]
    print(x)
    print(a)
f()
print(a)
