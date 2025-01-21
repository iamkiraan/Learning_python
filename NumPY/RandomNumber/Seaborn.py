from numpy import random as rnd
import matplotlib.pyplot as plt
import seaborn as sns


# sns.distplot([0, 1, 2, 3, 4, 5])

# # plt.show()

# # normal distribution
# x = rnd.normal(size=(2,3))
# print(x)

# # mean and standard deviation ko kura add garda

# y = rnd.normal(size=(2,3),loc=1,scale=4)
# print(y)

# # visualization of normal distribution
# sns.distplot(rnd.normal(size=100),hist=False)
# # plt.show()

# # binomial distribution
# k = rnd.binomial(p=0.2,n=10,size = 10)
# print(k)

# sns.distplot(rnd.binomial(p=0.5,n=10,size=1000),hist=True,kde = False)
# plt.show()

# difference between the normal and binomial distribution
sns.distplot(rnd.normal(loc=50, scale=5, size=1000), hist=False, label='normal')
sns.distplot(rnd.binomial(n=100, p=0.5, size=1000), hist=False, label='binomial')
plt.show()