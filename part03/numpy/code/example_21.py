import numpy as np
# Create 3 x 3 ndarray with repeated values
X = np.array([[1,2,3],[5,2,8],[1,2,3]])

# We print X
print()
print('X = \n', X)
print()

# We print the unique elements of X 
print('The unique elements in X are:',np.unique(X))
'''
X =
 [[1 2 3]
 [5 2 8]
 [1 2 3]]

The unique elements in X are: [1 2 3 5 8]
'''