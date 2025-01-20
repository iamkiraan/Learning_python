import numpy as np
arr = np.array([1,2,3,4])
x = arr.copy()
arr[0] = 23
print(x)
print(arr)

rra = np.array([1,4,5,6])
b = rra.view()
rra[0] = 23
print(rra)
print(b)

g = np.array([4,5,6,3,3])
c = g.copy()
d = g.view()

print(c.base)
print(d.base)