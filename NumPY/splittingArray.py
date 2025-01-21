import numpy as np

arr = np.array([1,2,3,4,5,6])
x = np.array_split(arr,6)
print(x)

# searching in array
result = np.array([1,2,3,4,56,7,8,5,3,2,21])
x = np.where(result ==4)
print(x)

# sorted array ma value rakhna lai
y = np.searchsorted(result,[7,9,0])
print(y)

# sorting the array
print(np.sort(arr))

arra = np.array(["kiiran","kiran","acharya","aacharya","the","main"])
print(np.sort(arra))