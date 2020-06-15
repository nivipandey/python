try:
	date=eval(input("entr date:"))
except SyntaxError:
	print("invalid")
else:
	print("you entered:",date)
