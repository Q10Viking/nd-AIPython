# We create a 2 x 3 ndarray full of fives.
import numpy as np 
X = np.full((2,3), 5) 

# We print X
print()
print('X = \n', X)
print()

# We print information about X
print('X has dimensions:', X.shape)
print('X is an object of type:', type(X))
print('The elements in X are of type:', X.dtype)
'''
X =
 [[5 5 5]
 [5 5 5]]

X has dimensions: (2, 3)
X is an object of type: <class 'numpy.ndarray'>
The elements in X are of type: int32
'''