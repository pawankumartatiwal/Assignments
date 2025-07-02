import numpy as np

arr_3d = np.arange(27).reshape(3, 3, 3)
moved = np.moveaxis(arr_3d, 0, -1)
print(moved)
