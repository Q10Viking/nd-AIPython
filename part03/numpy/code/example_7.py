# We create a 5 x 5 Identity matrix. 
import numpy as np
X = np.eye(5)

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
 [[1. 0. 0. 0. 0.]
 [0. 1. 0. 0. 0.]
 [0. 0. 1. 0. 0.]
 [0. 0. 0. 1. 0.]
 [0. 0. 0. 0. 1.]]

X has dimensions: (5, 5)
X is an object of type: <class 'numpy.ndarray'>
The elements in X are of type: float64
'''