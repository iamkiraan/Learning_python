import numpy as np
arr =np.array( [1,2,3,4,5])
print(arr)

# version checking
print(np.__version__)
print(type(arr))

# 0-D array

a = np.array(4) 
print(a)

# 1-D array
b = np.array([1,2,3,4])
print(b)

# 2-D array
c = np.array([[1,2,3,4],[5,6,7,8]])
print(c)

# 3-D array
d = np.array([[[1,2,3],[4,5,6]],[[2,3,4],[9,0,8]]])
print(d)

print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)

# higher dimension ma jana ko lagi
e = np.array([1,2,3,4],ndmin=5)
print(e)