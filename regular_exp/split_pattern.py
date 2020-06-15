import re
str=("this is\ regex demo\ using re")
res=re.split(r"\W+",str)
print(res)

