import numpy as np

arr = np.array([[6, -8, 73, -110], [np.nan, -8, 0, 94]])
arr = np.nan_to_num(arr)
arr = arr[:, :3].T
print(arr)

