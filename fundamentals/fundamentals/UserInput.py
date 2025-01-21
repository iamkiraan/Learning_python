import re

username = input("enter user name:\n")

try :
    if not isinstance(username,str):
     raise TypeError("username must be string")
    print("not matched nam,e")

except:
   print("internal errors")
