import numpy as np
# We create a rank 1 ndarray 
x = np.array([1, 2, 3, 4, 5])

# We create a rank 2 ndarray 
Y = np.array([[1,2,3],[4,5,6]])

# We print x
print()
print('Original x = ', x)

# We append the integer 6 to x
x = np.append(x, 6)

# We print x
print()
print('x = ', x)

# We append the integer 7 and 8 to x
x = np.append(x, [0,1])

# We print x
print()
print('x = ', x)

# We print x
print()
print('x = ', x)

# We print Y
print()
print('Original Y = \n', Y)

# We append a new row containing 7,8,9 to y
v = np.append(Y, [[7,8,9]], axis=0)

# We append a new column containing 9 and 10 to y
q = np.append(Y,[[9],[10]], axis=1)

# We print v
print()
print('v = \n', v)

# We print q
print()
print('q = \n', q)

'''
Original x =  [1 2 3 4 5]

x =  [1 2 3 4 5 6]

x =  [1 2 3 4 5 6 0 1]

x =  [1 2 3 4 5 6 0 1]

Original Y =
 [[1 2 3]
 [4 5 6]]

v =
 [[1 2 3]
 [4 5 6]
 [7 8 9]]

q =
 [[ 1  2  3  9]
 [ 4  5  6 10]]
 '''