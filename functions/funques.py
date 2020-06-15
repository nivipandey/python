def f(a,b):
    c=a+b
    d=a-b
    e=a*b
    f=a/b
    return c,d,e,f
x=int(input("enter one number"))
y=int(input("enter two number"))
r,s,t,u=f(x,y)
t1=(r,s,t,u)
print(t1)
