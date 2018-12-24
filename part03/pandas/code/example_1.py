# We import Pandas as pd into Python
import pandas as pd 

# We create a Pandas Series that stores a grocery list
groceries = pd.Series(data = [30, 6, 'Yes', 'No'], index = ['eggs', 'apples', 'milk', 'bread'])

# We display the Groceries Pandas Series
print(groceries)
'''
eggs       30
apples      6
milk      Yes
bread      No
dtype: object
'''

# We print some information about Groceries
print('Groceries has shape:', groceries.shape)
print('Groceries has dimension:', groceries.ndim)
print('Groceries has a total of', groceries.size, 'elements')
'''
Groceries has shape: (4,)
Groceries has dimension: 1
Groceries has a total of 4 elements
'''

# We check whether bananas is a food item (an index) in Groceries
x = 'bananas' in groceries

# We check whether bread is a food item (an index) in Groceries
y = 'bread' in groceries

# We print the results
print('Is bananas an index label in Groceries:', x)
print('Is bread an index label in Groceries:', y)
'''
Is bananas an index label in Groceries: False
Is bread an index label in Groceries: True
'''