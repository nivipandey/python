num=1
x=int(input("enter the limit"))
for i in range(x):
    for j in range(i+1):
        print(num,"",end="")
        num=num+1
    print("")
    num=1
