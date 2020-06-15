import logging
logging.basicConfig(filename='log.txt',level=logging.ERROR)
try:
	a=int(input("ener number:"))
	b=int(input("enter another"))
	c=a/b
except Exception as e:
	logging.exception(e)
else:
	print("dividion:",c)
