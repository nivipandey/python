a=5
b=0
print("exception demo")
try:
	c=a/b
	print(c)
except:
	print("zero division error")
finally:
	d=a+b
	print(d)
