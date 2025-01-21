# regular expression ho use to search a pattern
import re

text = "Nepal is a country those yes"
x = re.search("s",text)
if x :
    print("found")
else : 
    print("not found")

# findall use to return the list
x = re.findall("s",text)
if x:
    print(x)