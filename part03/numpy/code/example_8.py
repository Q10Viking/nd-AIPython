# Create a 4 x 4 diagonal matrix that contains the numbers 10,20,30, and 50
# on its main diagonal
import numpy as np
X = np.diag([10,20,30,50])

# We print X
print()
print('X = \n', X)
print()
'''
X =
 [[10  0  0  0]
 [ 0 20  0  0]
 [ 0  0 30  0]
 [ 0  0  0 50]]
 '''