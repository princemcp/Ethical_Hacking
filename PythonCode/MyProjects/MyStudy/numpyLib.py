import numpy as np

# Create a 3x3 identity matrix
identity_matrix = np.eye(3)

print(identity_matrix)



 #Create a 1D array
arr1d = np.array([1, 2, 3, 4, 5])
print(arr1d)


# Create a 2D array (matrix)
arr2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(arr2d)



# Create an array of zeros
zeros = np.zeros((3, 3))
print(zeros)



# Create an array of ones
ones = np.ones((2, 4))
print(ones)



# Create an identity matrix
identity = np.eye(3)


 #Get the shape of an array
shape = arr2d.shape  # (3, 3)
print(shape)

# Get the data type of elements in an array
dtype = arr1d.dtype  # int64
print(dtype)

# Get the number of dimensions
ndim = arr2d.ndim  # 2
print(ndim)