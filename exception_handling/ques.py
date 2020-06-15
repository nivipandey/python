import logging
logging.basicConfig(filename="log.txt",level=logging.ERROR)
try:
           a=12
           b="abc"
           c=a+b
except TypeError as typ:
          print("cannot add number and string")
          logging.exception(typ)
  
try:
          l=[1,2,3,4]
          print(l[8])
except IndexError as indx:
          print("index 8 doesnot exist")
          logging.exception(indx)
 
  
try:
          num=12
          num1=0
          s=num/num1
          print(s);
except ZeroDivisionError as zero:
          print("cannot add number and string")
          logging.exception(zero)
else:
          print("all throws exception")
  
finally:
 	print("successful")
  

