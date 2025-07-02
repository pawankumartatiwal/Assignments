import numpy as np

arr = np.array([[3, -5, 7], [-2, 9, -1]])
arr[arr < 0] = 0
print(arr)
