class MyException(Exception):
	def __init__(self,arg):
		self.msg=arg
def check(dict):
	for k,v in dict.items():
		print("name {} balance={}".format(k,v))
		if(v<2000):
			raise MyException("balance amount less"+k)
bank={"arun":5000,"cdac":8483,"pep":139,"naresh":3600}
try:
	check(bank)
except MyException as error:
	print(error)

