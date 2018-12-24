# We create a 3 x 3 ndarray with random floats in the half-open interval [0.0, 1.0).
import numpy as np
# We create a 3 x 2 ndarray with random integers in the half-open interval [4, 15).
X = np.random.randint(4,15,size=(3,2))

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
 [[11 10]
 [14 13]
 [ 9  7]]

X has dimensions: (3, 2)
X is an object of type: <class 'numpy.ndarray'>
The elements in X are of type: int32
'''