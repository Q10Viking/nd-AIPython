# We create a rank 1 ndarray that has evenly spaced integers from 1 to 13 in steps of 3.
import numpy as np
x = np.arange(1,14,3)

# We print the ndarray
print()
print('x = ', x)
print()

# We print information about the ndarray
print('x has dimensions:', x.shape)
print('x is an object of type:', type(x))
print('The elements in x are of type:', x.dtype) 
'''
x =  [ 1  4  7 10 13]

x has dimensions: (5,)
x is an object of type: <class 'numpy.ndarray'>
The elements in x are of type: int32
'''