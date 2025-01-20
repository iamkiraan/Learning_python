import numpy as np
arr1 = np.array([1,2,3,4])
arr2 = np.array([6,7,8])
arr = np.concatenate((arr1,arr2))
print(arr)

# 2-D array sanga kaam garda
xt = np.array([[1,2,3],[4,5,6]])
yt = np.array([[3,2,1],[6,5,4]])
xyt = np.concatenate((xt,yt),axis=1)
print(xyt)
# instead helper function hstack can also be used
xp = np.array([[1,2,3],[4,5,6]])
yp = np.array([[3,2,1],[6,5,4]])
# xyp= np.hstack((xp,yp))
# xyp = np.vstack((xp,yp))
xyp = np.dstack((xp,yp))
print(xyp)
