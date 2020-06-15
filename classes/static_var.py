class sample:
	x=20
	#this is a class method we use a build in decorator statement
	@classmethod
	def method1(self):
		self.x=self.x+1
a1=sample()
a2=sample()
print(a1.x)
a1.method1()
print(a1.x)
print(a2.x)
