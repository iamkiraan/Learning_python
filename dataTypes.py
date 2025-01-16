# data types in python
x = [1,2,3,4]
x = range(6)
x = {"name" : "kiran","age" : 23}
x = frozenset({"kiran","acharya"})
x = True
print(type(x))

# numbers in python
# integer
# float
# complex

x= -3
x = -3.45
x = 3+5j
print(type(x))

import random as value
print(value.randrange(1,10))

# slicing string
y = "  kiranacharya  "
a = y[-7:]
b = y[:5]
print(a+b)

print(y.upper())
print(y.strip())
print(y.replace('a','L'))
print(y.split(','))

# merging a variable
a = "kiran acharya"
b = "from kalikot"
c= a + b
print(c)
c = a + "" + b
print(c)

age = 23
text = f"kiran acharya{age}"
print(text)
