'''
NumPy is a python package. It stands for 'Numerical Python'. It is a library consisting of 
multidimensional array objects and a collection of routines for processing of array.

The most important object defined in NumPy is an N-dimensional array type called ndarray.
It describes the collection of items of the same type. Items in the collection can be accessed using 
a zero-based index. Every item in an ndarray takes the same size of block in the memory. 
Each element in ndarray is an object of data-type object (called dtype).

Standard Python distribution doesn't come bundled with NumPy module. A lightweight alternative is to
install NumPy using popular Python paciage instaler, pip.
pip install numpy
'''

import numpy as np

# example 1

# lst = [1, 2, 3]
# arr = np.array(lst)
# print(arr, arr.ndim)

# example 2

# lst = [[2, 4, 6], [0, 1, 3]]
# arr = np.array(lst)
# print(arr)
# print(arr.shape)
# print(arr.ndim)

# example 3

# arr1 = np.array([1, 2, 3, 4, 5])
# arr2 = np.array([3, 4, 5, 1, 3])

# out = arr1 + arr2
# print(out)

# example 4

# arr1 = np.array([1, 2, 3, 4, 5, 6])
# arr2 = np.array([3, 4, 5, 1, 3, 3])

# m1 = arr1.reshape((3, 2))
# m2 = arr2.reshape((2, 3))

# print(m1)

# example 5

arr1 = np.array([1, 2, 3, 4, 5, 6])
arr2 = np.array([3, 4, 5, 1, 3, 3])

arr1 = arr1.reshape((2, 3))
arr2 = arr2.reshape((2, 3))

out = np.multiply(arr1, arr2)
print(out)