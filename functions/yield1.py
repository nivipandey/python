def gen(x,y):
    while x<=y:
        yield x
        x=x+1
g=gen(5,10)
print("type of g is",type(g))
t=tuple(gen(5,10))
print(t)
print("type of t",type(t))
for i in g:
    print(i)
