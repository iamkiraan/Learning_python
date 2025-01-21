import numpy as np

arr = np.array([1,2,3,4,434,23,65,12,21,42,6,646,34])

newArr = []

for elements in arr:
    if elements>20:
        newArr.append(True)
    else: 
        newArr.append(False)

filer_arr = arr[newArr]
print(newArr)
print(filer_arr)
