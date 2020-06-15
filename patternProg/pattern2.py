num=1
n=int(input("enter the limit"))
for x in range(n):
    for y in range(x+1):
        print(num,end="")
        num=num+1
    num=1
    print("")
    
