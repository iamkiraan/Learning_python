# two ways of ararngement of the elements
from numpy import random as rnd
import numpy as np


x = np.array([1,2,3,4])
rnd.shuffle(x)
print(x)

# also can be done as
rnd.permutation(x)
print(x)

# both gives same value after arrangement of the array