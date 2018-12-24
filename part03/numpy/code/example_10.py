# We create a rank 1 ndarray that has 10 integers evenly spaced between 0 and 25.
import numpy as np
x = np.linspace(0,25,10)

# We print the ndarray
print()
print('x = \n', x)
print()

# We print information about the ndarray
print('x has dimensions:', x.shape)
print('x is an object of type:', type(x))
print('The elements in x are of type:', x.dtype)
'''
x =
 [ 0.          2.77777778  5.55555556  8.33333333 11.11111111 13.88888889
 16.66666667 19.44444444 22.22222222 25.        ]

x has dimensions: (10,)
x is an object of type: <class 'numpy.ndarray'>
The elements in x are of type: float64
'''