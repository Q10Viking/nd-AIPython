import pandas as pd
# We create a Pandas Series that stores a grocery list of just fruits
fruits= pd.Series(data = [10, 6, 3,], index = ['apples', 'oranges', 'bananas'])

# We print fruits for reference
print('Original grocery list of fruits:\n ', fruits)

# We perform basic element-wise operations using arithmetic symbols
print()
print('fruits + 2:\n', fruits + 2) # We add 2 to each item in fruits
print()
print('fruits - 2:\n', fruits - 2) # We subtract 2 to each item in fruits
print()
print('fruits * 2:\n', fruits * 2) # We multiply each item in fruits by 2 
print()
print('fruits / 2:\n', fruits / 2) # We divide each item in fruits by 2
print()
'''
Original grocery list of fruits:
  apples     10
oranges     6
bananas     3
dtype: int64

fruits + 2:
 apples     12
oranges     8
bananas     5
dtype: int64

fruits - 2:
 apples     8
oranges    4
bananas    1
dtype: int64

fruits * 2:
 apples     20
oranges    12
bananas     6
dtype: int64

fruits / 2:
 apples     5.0
oranges    3.0
bananas    1.5
dtype: float64
'''