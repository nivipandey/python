from datetime import *
d,m,y=[int(x) for x in input("enter a date").split("-")]
dt=date(y,m,d)
s1=dt.strftime("%j")
print("day",s1)
s2=dt.strftime("%A")
print("week:,",s2)
