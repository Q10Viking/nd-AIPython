# We create a 3 x 2 ndarray full of ones. 
import numpy as np
X = np.ones((3,2))

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
 [[1. 1.]
 [1. 1.]
 [1. 1.]]

X has dimensions: (3, 2)
X is an object of type: <class 'numpy.ndarray'>
The elements in X are of type: float64
'''