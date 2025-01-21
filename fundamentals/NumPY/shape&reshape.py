import numpy as np

arr = np.array([[1,2,3,4],[3,4,5,6]])
print(arr.shape)

# fifth dimension ko lagi

a = np.array([1,2,3,4],ndmin=5)
print(a)
print(a.shape)

# reshaping the 1-D array to 2-D array

b = np.array([1,2,3,4,5,6,7,8])
x = b.reshape(4,2)
print(x)

# changing 1-d into 3-d
f = b.reshape(2,2,2)
print(f)