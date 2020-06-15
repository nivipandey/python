#pattern 6
print("")
n = int(input("enter the limit"))
g = n
h = n-1
for x in range(0,n):
    
    for y in range(0,h):
        print("",end=" ")
    h-=1
        
    for b in range(0,x+1):
        print("*",end=" ")
    print("")
