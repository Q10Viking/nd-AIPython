import numpy as np
# We create an unsorted rank 1 ndarray
x = np.random.randint(1,11,size=(10,))

# We print x
print()
print('Original x = ', x)

# We sort x and print the sorted array using sort as a function.
print()
print('Sorted x (out of place):', np.sort(x))

# When we sort out of place the original array remains intact. To see this we print x again
print()
print('x after sorting:', x)
'''
Original x =  [ 4  6  5  9  5  9  9 10  9  2]

Sorted x (out of place): [ 2  4  5  5  6  9  9  9  9 10]

x after sorting: [ 4  6  5  9  5  9  9 10  9  2]
'''