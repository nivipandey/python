l1=[1,2,3,4,5,6]
su=0
for i in l1:
    su=su+i
print(su)
x=len(l1)
while x != l1[-1]:
    su=su+l1[x]
    x+=1
print(su)
