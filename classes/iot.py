class iot:
	def __init__(self):
		self.id=123
		self.name="sudi"
	def cdac(self):
		print(self.id)
		print(self.name)
s1=iot()
s2=iot()
s3=iot()
print(id(s1))
print(id(s2))
print(id(s3))
s1.cdac()
s2.cdac()
s3.cdac()

