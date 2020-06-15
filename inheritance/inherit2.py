class a():
	def arun(self):
		print("hello")
	def arun(self):
		print("this is method 2")
	def arun(self):
		print("this is m3")
class b(a):
	def arun(self):
		print("rest")
class c(a):
	def xyz(self):
		print("xyz")
class d(a,b):
	def abc(self):
		print("abc")
dobj=d()
dobj.arun()
dobj.arun()
dobj.abc()
