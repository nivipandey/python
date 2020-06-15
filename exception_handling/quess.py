l=[]
x=int(input("enter how many values"))
for i in range(0,x):
	a=int(input("enter the number"))
	l.append(a)
class cdac(Exception):
	def __init__(self,arg):
		self.msg=arg
def check(l):
	for a in l:
		print("element :",a)
		if(a>50):
			raise cdac("element should not be graeter than 50")
try:
	check(l)
except cdac as error:
	print(error)
