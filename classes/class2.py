class abc():
	a=10
	b=20
	def m1(self): #check by excluding self parameter from the function :
		print("this is one")
	def m2(self):
		print("this is two")
object1=abc()
print(object1.a)
object1.m1()
object1.m2()
