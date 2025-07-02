import numpy as np
from scipy import stats

arr1 = np.array([3, 4])
arr2 = np.array([1, 0])
avg = (arr1 + arr2) / 2
print(avg)

arr3 = np.array([[1, 2, 3], [4, 5, 6]])
arr4 = np.array([[6, 5, 4], [3, 2, 1]])
combined = (arr3 + arr4) / 2
print(combined)
print(np.mean(combined))
print(np.median(combined))
print(stats.mode(combined, axis=None, keepdims=True).mode[0])
