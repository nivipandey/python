import time
l=[1,2,3,4,5,"j","i","t","u"]
l[5]="pagol"
print(l)
time.sleep(2)


l.append(31)
print(l)

time.sleep(2)

l.extend(["i","love","you"])
print(l)

time.sleep(2)
l.append(["pagol","and","pagoli"])
print(l)

time.sleep(2)
l.insert(2,"123")
print(l)

time.sleep(2)
l[6:2]=[99,98,76]
print(l)

time.sleep(2)


del l[2]
print(l)

time.sleep(1)

l.remove(["pagol","and","pagoli"])
print(l)


time.sleep(2)

l.clear()
print(l)

print(l.index(99,[2,[7]]))


