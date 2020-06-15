class sample:
	def __init__(self):
		self.x=20
	def m1(self):
		self.x=self.x+1
s1=sample()
s2=sample()
print(s1.x)
print(s2.x)
s1.m1()
print(s1.x)
print(s2.x)

