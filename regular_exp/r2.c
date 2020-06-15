import re
str = "sat bat bath mant bjdk"
result = re.search(r"m\w\w",str)
if result: 
        print(result.group)
