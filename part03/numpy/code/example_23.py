import numpy as np
# We create a rank 1 ndarray
x = np.array([1,2,3,4,5])

# We create a rank 1 ndarray
y = np.array([6,7,2,8,4])

# We print x
print()
print('x = ', x)

# We print y
print()
print('y = ', y)

# We use set operations to compare x and y:
print()
print('The elements that are both in x and y:', np.intersect1d(x,y))
print('The elements that are in x that are not in y:', np.setdiff1d(x,y))
print('All the elements of x and y:',np.union1d(x,y))

'''
x =  [1 2 3 4 5]

y =  [6 7 2 8 4]

The elements that are both in x and y: [2 4]
The elements that are in x that are not in y: [1 3 5]
All the elements of x and y: [1 2 3 4 5 6 7 8]
'''