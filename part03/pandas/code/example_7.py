import pandas as pd
# We create a list of Python dictionaries
items2 = [{'bikes': 20, 'pants': 30, 'watches': 35, 'shirts': 15, 'shoes':8, 'suits':45},
{'watches': 10, 'glasses': 50, 'bikes': 15, 'pants':5, 'shirts': 2, 'shoes':5, 'suits':7},
{'bikes': 20, 'pants': 30, 'watches': 35, 'glasses': 4, 'shoes':10}]

# We create a DataFrame  and provide the row index
store_items = pd.DataFrame(items2, index = ['store 1', 'store 2', 'store 3'])

# We display the DataFrame
print(store_items)
'''
         bikes  glasses  pants  shirts  shoes  suits  watches
store 1     20      NaN     30    15.0      8   45.0       35
store 2     15     50.0      5     2.0      5    7.0       10
store 3     20      4.0     30     NaN     10    NaN       35
'''
# We count the number of NaN values in store_items
x =  store_items.isnull().sum().sum()

# We print x
print('Number of NaN values in our DataFrame:', x)
'''
Number of NaN values in our DataFrame: 3
'''

print(store_items.isnull())
'''
         bikes  glasses  pants  shirts  shoes  suits  watches
store 1  False     True  False   False  False  False    False
store 2  False    False  False   False  False  False    False
store 3  False    False  False    True  False   True    Fals
'''
print(store_items.isnull().sum())
'''
bikes      0
glasses    1
pants      0
shirts     1
shoes      0
suits      1
watches    0
dtype: int64
'''
# We drop any rows with NaN values
print(store_items.dropna(axis = 0))
'''
         bikes  glasses  pants  shirts  shoes  suits  watches
store 2     15     50.0      5     2.0      5    7.0       10
'''
# We drop any columns with NaN values
print(store_items.dropna(axis = 1))
'''
         bikes  pants  shoes  watches
store 1     20     30      8       35
store 2     15      5      5       10
store 3     20     30     10       35
'''
# We replace all NaN values with 0
print(store_items.fillna(0))
'''
         bikes  glasses  pants  shirts  shoes  suits  watches
store 1     20      0.0     30    15.0      8   45.0       35
store 2     15     50.0      5     2.0      5    7.0       10
store 3     20      4.0     30     0.0     10    0.0       35
'''
# We replace NaN values with the previous value in the column
print(store_items.fillna(method = 'ffill', axis = 0))
'''         bikes  glasses  pants  shirts  shoes  suits  watches
store 1     20      NaN     30    15.0      8   45.0       35
store 2     15     50.0      5     2.0      5    7.0       10
store 3     20      4.0     30     2.0     10    7.0       35
'''
# We replace NaN values with the previous value in the row
print(store_items.fillna(method = 'ffill', axis = 1))
'''
         bikes  glasses  pants  shirts  shoes  suits  watches
store 1   20.0     20.0   30.0    15.0    8.0   45.0     35.0
store 2   15.0     50.0    5.0     2.0    5.0    7.0     10.0
store 3   20.0      4.0   30.0    30.0   10.0   10.0     35.0
'''
# We replace NaN values with the next value in the row
print(store_items.fillna(method = 'backfill', axis = 1))
'''
         bikes  glasses  pants  shirts  shoes  suits  watches
store 1   20.0     30.0   30.0    15.0    8.0   45.0     35.0
store 2   15.0     50.0    5.0     2.0    5.0    7.0     10.0
store 3   20.0      4.0   30.0    10.0   10.0   35.0     35.0
'''
# We replace NaN values by using linear interpolation using column values
print(store_items.interpolate(method = 'linear', axis = 1))
'''
         bikes  glasses  pants  shirts  shoes  suits  watches
store 1   20.0     25.0   30.0    15.0    8.0   45.0     35.0
store 2   15.0     50.0    5.0     2.0    5.0    7.0     10.0
store 3   20.0      4.0   30.0    20.0   10.0   22.5     35.0
'''