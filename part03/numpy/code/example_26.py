import numpy as np
# We create a rank 1 ndarray
x = np.array([1,2,3])

# We create a 3 x 3 ndarray
Y = np.array([[1,2,3],[4,5,6],[7,8,9]])

# We create a 3 x 1 ndarray
Z = np.array([1,2,3]).reshape(3,1)

# We print x
print()
print('x = ', x)
print()

# We print Y
print()
print('Y = \n', Y)
print()

# We print Z
print()
print('Z = \n', Z)
print()

print('x + Y = \n', x + Y)
print()
print('Z + Y = \n',Z + Y)
'''
x =  [1 2 3]


Y =
 [[1 2 3]
 [4 5 6]
 [7 8 9]]


Z =
 [[1]
 [2]
 [3]]

x + Y =
 [[ 2  4  6]
 [ 5  7  9]
 [ 8 10 12]]

Z + Y =
 [[ 2  3  4]
 [ 6  7  8]
 [10 11 12]]
 '''