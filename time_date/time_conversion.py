import time
epoch=time.time()
t=time.localtime(epoch)
d=t.tm_mday
m=t.tm_mon
y=t.tm_year
print("current date is:",d,m,y)
