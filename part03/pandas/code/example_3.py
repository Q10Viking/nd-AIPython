# We import Pandas as pd into Python
import pandas as pd 

# We create a Pandas Series that stores a grocery list
groceries = pd.Series(data = [30, 6, 'Yes', 'No'], index = ['eggs', 'apples', 'milk', 'bread'])

# We display the original grocery list
print('Original Grocery List:\n', groceries)

# We remove apples from our grocery list. The drop function removes elements out of place
print()
print('We remove apples (out of place):\n', groceries.drop('apples'))

# When we remove elements out of place the original Series remains intact. To see this
# we display our grocery list again
print()
print('Grocery List after removing apples out of place:\n', groceries)
'''
Original Grocery List:
 eggs       30
apples      6
milk      Yes
bread      No
dtype: object

We remove apples (out of place):
 eggs      30
milk     Yes
bread     No
dtype: object

Grocery List after removing apples out of place:
 eggs       30
apples      6
milk      Yes
bread      No
dtype: object
'''

# We display the original grocery list
print('Original Grocery List:\n', groceries)

# We remove apples from our grocery list in place by setting the inplace keyword to True
groceries.drop('apples', inplace = True)

# When we remove elements in place the original Series its modified. To see this
# we display our grocery list again
print()
print('Grocery List after removing apples in place:\n', groceries)
'''
Original Grocery List:
 eggs       30
apples      6
milk      Yes
bread      No
dtype: object

Grocery List after removing apples in place:
 eggs      30
milk     Yes
bread     No
dtype: object
'''