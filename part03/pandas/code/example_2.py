# We import Pandas as pd into Python
import pandas as pd 

# We create a Pandas Series that stores a grocery list
groceries = pd.Series(data = [30, 6, 'Yes', 'No'], index = ['eggs', 'apples', 'milk', 'bread'])

# We access elements in Groceries using index labels:

# We use a single index label
print('How many eggs do we need to buy:', groceries['eggs'])
print()

# we can access multiple index labels
print('Do we need milk and bread:\n', groceries[['milk', 'bread']]) 
print()

# we use loc to access multiple index labels
print('How many eggs and apples do we need to buy:\n', groceries.loc[['eggs', 'apples']]) 
print()

# We access elements in Groceries using numerical indices:

# we use multiple numerical indices
print('How many eggs and apples do we need to buy:\n',  groceries[[0, 1]]) 
print()

# We use a negative numerical index
print('Do we need bread:\n', groceries[[-1]]) 
print()

# We use a single numerical index
print('How many eggs do we need to buy:', groceries[0]) 
print()
# we use iloc to access multiple numerical indices
print('Do we need milk and bread:\n', groceries.iloc[[2, 3]])
'''
How many eggs do we need to buy: 30

Do we need milk and bread:
 milk     Yes
bread     No
dtype: object

How many eggs and apples do we need to buy:
 eggs      30
apples     6
dtype: object

How many eggs and apples do we need to buy:
 eggs      30
apples     6
dtype: object

Do we need bread:
 bread    No
dtype: object

How many eggs do we need to buy: 30

Do we need milk and bread:
 milk     Yes
bread     No
dtype: object
'''