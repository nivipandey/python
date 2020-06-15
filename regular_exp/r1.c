import re
str = "cat rat bat  math nat sat mat pat"
result = re.search(r"m\w\w\w",str)
print(result.group())
