fname=input("enter fisrt name")
lname=input("enter string last name:")
a=int(input("enter age"))
b=int(input("enter salary"))
name=fname+lname
print("Name : " +name)
print("3rd " +name[3])
print("-3rd" +name[-3])
print("bin of age : "+str(bin(a)))
print("bin of salary : "+str(bin(b)))
print(type(a))
print(type(name))
print(fname[0])
print(lname[-1])
print("length")
print(len(fname))
print("count frst letter")
print(fname.count(fname[0]))
print()
print("find k")
print(fname.find("k"))
print(name[1:-1:2])

