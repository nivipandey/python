import re
str = "GVR is founder of puthon and also founder of abc programming language intial poor"
result=re.sub(r"abc","XYZ",str)
print (result)
result1 = re.search(r"m\w\w\w",str)
print(result1.group())
