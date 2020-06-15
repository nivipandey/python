try:
	x=int(input("enter a number between 5 and 10"))
	assert x>=5 and x<=10
	print("the number entered:",x)
except AssertionError:
	print("the condition is not fulfilled:")
