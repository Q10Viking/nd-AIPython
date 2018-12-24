import numpy as np
# We create a rank 1 ndarray 
x = np.array([1, 2, 5, 6, 7])

# We create a rank 2 ndarray 
Y = np.array([[1,2,3],[7,8,9]])

# We print x
print()
print('Original x = ', x)

# We insert the integer 3 and 4 between 2 and 5 in x. 
x = np.insert(x,2,[3,4])

# We print x with the inserted elements
print()
print('x = ', x)

# We print Y
print()
print('Original Y = \n', Y)

# We insert a row between the first and last row of y
w = np.insert(Y,1,[4,5,6],axis=0)

# We insert a column full of 5s between the first and second column of y
v = np.insert(Y,1,[5,6], axis=1)

# We print w
print()
print('w = \n', w)

# We print v
print()
print('v = \n', v)

'''
Original x =  [1 2 5 6 7]

x =  [1 2 3 4 5 6 7]

Original Y =
 [[1 2 3]
 [7 8 9]]

w =
 [[1 2 3]
 [4 5 6]
 [7 8 9]]

v =
 [[1 5 2 3]
 [7 6 8 9]]
 '''