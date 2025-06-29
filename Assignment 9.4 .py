import numpy as np

a = np.array([[3, 7, 1], [8, 5, 2]])

# Maximum and minimum values
print(a.max())    
print(a.min())     

# Number of rows and columns
print(a.shape[0], a.shape[1]) 

# Print all elements
for row in a:
    for val in row:
        print(val)

# Access specific element
print(a[1, 2])  # element at 2nd row, 3rd column

# Sum using for loop
total = 0
for row in a:
    for val in row:
        total += val
print(total)

# Array arithmetic
x = np.array([1, 2, 3])
y = np.array([4, 5, 6])

print(x + y)  
print(x - y)  
print(x * y) 
print(x / y)  
