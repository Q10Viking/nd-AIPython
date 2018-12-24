# We create a 3 x 4 ndarray full of zeros.
import numpy as np 
X = np.zeros((3,4))

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
 [[0. 0. 0. 0.]
 [0. 0. 0. 0.]
 [0. 0. 0. 0.]]

X has dimensions: (3, 4)
X is an object of type: <class 'numpy.ndarray'>
The elements in X are of type: float64
'''