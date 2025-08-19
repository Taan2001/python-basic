# to install, run cmd: pip install numpy
# to use:
# use: import numpy as np
"""
    AI Coding
"""

import numpy as np

# 1. Create 1-dimensional array
arr = np.array([1, 2, 3, 4, 5, 6.0, 'a'])
print(arr)
print(type(arr))
print(arr.dtype)

# 2. Get value by index
print(f"The first element: {arr[0]}")
print(f"The last element: {arr[-1]}")

# 3. Slice => no return a copy 
new_array1 = arr[0:2]
new_array1[1] = 3
new_array2 = arr[-4:-1]
print(f"The element: {new_array1}")
print(f"The element: {new_array2}")
print(f"The arr: {arr}")

# 4. create 2 dimensional array
array_2d = np.array([[1, 2, 3], [4, 5, 6], ['a', 'b', 'c']])
# array_2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8]]) # error
print(array_2d)
print(type(array_2d))

# 5. Get value in 2 dimensional array
print("first row & first column:", array_2d[0][0])
print("first row & first column:", array_2d[0, 0])
print("second row & second column:", array_2d[1][1])
print("Get first row:", array_2d[0, :])
print("Get first column:", array_2d[:, 0])

# 6.ndim - determine the dimension of the array
arr_1d = np.array([1, 2, 3, 4, 5])
arr_2d = np.array([[1, 2, 3], [4, 5, 6], [6, 7, 8]])

print(f"The dimension: {arr_1d.ndim}")
print(f"The dimension: {arr_2d.ndim}")

# 7. shape - get element in each dimension => return tuple
print(f"Shap of 1d array:", arr_1d.shape)
print(f"Shap of 2d array:", arr_2d.shape)

# 8. size - get size of array
print(f"Size of 1d array:", arr_1d.size)
print(f"Size of 2d array:", arr_2d.size)

# 9. as - create new and convert type for array
arr_1d = np.array([1, 2, 3, 4])
new_arr_1d = arr_1d.astype(np.float64)
arr_2d = np.array([[1, 2, 3], [4, 5, 6], [6, 7, 8]])

print(f"1d array:", arr_1d)
print(f"Type of 1d array:", arr_1d.dtype)
print(f"new 1d array:", new_arr_1d)
print(f"Type of new 1d array:", new_arr_1d.dtype)

# 10. Create with zero value array
zeros_array = np.zeros((4, ))
print(zeros_array)

# 11. Create with one value array
ones_array = np.ones((4, 4))
print(ones_array)

# 12. Create with range value array
range_array1 = np.arange(10)
print(range_array1)

range_array2 = np.arange(1, 10, 2, 'float64')
print(range_array2) # 1 3 4 5 7 9

range_array2 = np.arange(0, 10, 2, 'float64')
print(range_array2) # 0 2 4 6 8

# 13. linespace
linspace_arr = np.linspace(0, 10, num = 6)
print(linspace_arr) # 0 2 4 6 8 10

"""
    Arithmetic - Array
"""
arr_1= np.array([1, 2, 3, 4])
arr_2= np.array([5, 6, 7, 8])
# arr_2= np.array([5, 6, 7]) # error

# Add: + ==> arr_1.shape == arr_2.shape
result = arr_1 + arr_2
print(f"result Add: {result}")
print(f"shape: {arr_1.shape == arr_2.shape}")

# Sub: - ==> arr_1.shape == arr_2.shape
result = arr_2 - arr_1
print(f"result Sub: {result}")

# Mul: * ==> arr_1.shape == arr_2.shape
result = arr_2 * arr_1
print(f"result Mul: {result}")

# Div: / ==> arr_1.shape == arr_2.shape
result = arr_2 / arr_1
print(f"result Div: {result}")

# sum 
arr_1 = np.array([1, 2, 3, 4])
print(arr_1)
print(f"Sum of arr_1: {arr_1.sum()}")
print(f"Sum of arr_1: {np.sum(arr_1)}")

arr_2d = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
row_sum = arr_2d.sum(axis = 1, keepdims = True)
column_sum = arr_2d.sum(axis = 0, keepdims = True)

print(f"sum of each row: {arr_2d.sum(axis = 1)}")
print(f"sum of each row: {row_sum}")
print(f"sum of each row: {row_sum.shape}")
print(f"sum of each column: {arr_2d.sum(axis = 0)}")
print(f"sum of each column: {column_sum}")
print(f"sum of each column: {column_sum.shape}")

# Min, Max, Mean 
print(f"Min: {arr_2d.min()}")
print(f"Max: {arr_2d.max()}")
print(f"Mean: {arr_2d.mean()}")

"""
    Boardcasting
"""
arr_1 = np.array([[4, 5, 6], [7, 8, 9]])
arr_2 = np.array([1, 2, 3])
arr_3 = np.array([[1], [2]])
my_result1 = arr_1 + arr_2
my_result2 = arr_1 + arr_3
print(f"my result1: {my_result1}")
print(f"my result2: {my_result2}")

"""
    Reshape
"""
print(np.reshape(arr_3, (2, )))
print(arr_3.reshape((2, )))

"""
    Flatten
"""
print(arr_1.flatten())
