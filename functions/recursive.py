def f1(n):
    if n==0:
        result=1
    else:
        result=n*f1(n-1)
    return result
for i in range(1,11):
    print("fact of {} is {}".format(i,f1(i)))
