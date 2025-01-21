import numpy as np
arr = np.array([1,2,3,4])

for x in arr:
    print(x)

print("\n")
for x in arr:
    if x%2 == 0:
        print(x)

# how 2 d array is printed

b = np.array([[1,2,3],[5,6,7]])
for x in b:
    # if x>4:
    print(x)

# iterating down the 2-D array
value = np.array([[1,2,3],[5,6,7]])
for x in value:
    for y in x:
        print(y)

# how 3-D array is printed
crray = np.array([[[1,2,3],[4,5,6]],[[11,12,13],[14,15,16]]])
for x in crray:
    print(x)

# iterating through 3-D array

# for x in crray:
#     for y in x:
#         for z in y:
#             print(z)
#  nditr le iteration through janu pardaina
for x in np.nditer(crray):
    print(x)