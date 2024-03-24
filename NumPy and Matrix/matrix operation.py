import numpy as np

# task 1 - array reverse

# lst = list(map(float, input("Enter array elements : ").split()))
# arr = np.array(lst, dtype=float)
# out = np.flip(arr)
# print(out)

# task 2 - array reshape

# lst = list(map(int, input("Enter 9 elements : ").split()))
# arr = np.array(lst)
# out = arr.reshape((3, 3))
# print(out)

# task 3 - identity matrix

# n, m = map(int, input("Rows & Columns : ").split())
# out = np.eye(n, m)
# # out = np.identity(n) # works for square identity matrix
# print(out)

# task 4 - matrix calculations

# n, m = map(int, input("Rows & Columns : ").split())
# arr1 = np.array(list(map(int, input("Enter array 1 elements : ").split()))).reshape((n, m))
# arr2 = np.array(list(map(int, input("Enter array 2 elements : ").split()))).reshape((n, m))

# print("\nARR_1 + ARR_2 : \n", np.add(arr1, arr2))
# print("\nARR_1 - ARR_2 : \n", np.subtract(arr1, arr2))
# print("\nARR_1 x ARR_2 : \n", np.multiply(arr1, arr2))
# print("\nARR_1 / ARR_2 : \n", np.divide(arr1, arr2))
# print("\nARR_1 // ARR_2 : \n", np.floor_divide(arr1, arr2))
# print("\nARR_1 ^ ARR_2 : \n", np.power(arr1, arr2))
# print("\nARR_1 % ARR_2 : \n", np.remainder(arr1, arr2))

# task 5 - flatten and trasnpose of matrix

# n, m = map(int, input("Rows & Columns : ").split())
# arr = np.array(list(map(int, input("Enter array elements : ").split()))).reshape((n, m))
# arr_t = np.transpose(arr)
# print(arr_t)

