from numpy import random as rnd

x = rnd.rand()
print(x)

# array ko lagi 
y = rnd.randint(10,size=5)
print(y)

# 2-D array ko lagi
z = rnd.randint(100,size=(2,3))
print(z)

# random choices ko lagi
v = rnd.choice([2,3,4,5])
print(v)