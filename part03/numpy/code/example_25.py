import numpy as np
# We create an unsorted rank 2 ndarray
X = np.random.randint(1,11,size=(5,5))

# We print X
print()
print('Original X = \n', X)
print()

# We sort the columns of X and print the sorted array
print()
print('X with sorted columns :\n', np.sort(X, axis = 0))

# We sort the rows of X and print the sorted array
print()
print('X with sorted rows :\n', np.sort(X, axis = 1))
'''
Original X =
 [[ 5  5  1  6  5]
 [ 3  5  2  7 10]
 [ 8  2  2  5  8]
 [ 3  4  2  2 10]
 [ 4  4  1  6 10]]


X with sorted columns :
 [[ 3  2  1  2  5]
 [ 3  4  1  5  8]
 [ 4  4  2  6 10]
 [ 5  5  2  6 10]
 [ 8  5  2  7 10]]

X with sorted rows :
 [[ 1  5  5  5  6]
 [ 2  3  5  7 10]
 [ 2  2  5  8  8]
 [ 2  2  3  4 10]
 [ 1  4  4  6 10]]
 '''