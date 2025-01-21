from numpy import random as rnd
import matplotlib.pyplot as plt
import seaborn as sns


sns.distplot([0, 1, 2, 3, 4, 5])

# plt.show()

# normal distribution
x = rnd.normal(size=(2,3))
print(x)

# mean and standard deviation ko kura add garda

y = rnd.normal(size=(2,3),loc=1,scale=4)
print(y)

# visualization of normal distribution
sns.distplot(rnd.normal(size=100),hist=False)
plt.show()