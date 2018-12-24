# We import Pandas as pd into Python
import pandas as pd
# We create a list of Python dictionaries
items2 = [{'bikes': 20, 'pants': 30, 'watches': 35}, 
          {'watches': 10, 'glasses': 50, 'bikes': 15, 'pants':5}]

# We create a DataFrame 
store_items = pd.DataFrame(items2)

# We display the DataFrame
print(store_items)
'''
   bikes  glasses  pants  watches
0     20      NaN     30       35
1     15     50.0      5       10
'''

# We create a DataFrame  and provide the row index
store_items = pd.DataFrame(items2, index = ['store 1', 'store 2'])
print(store_items)
'''
         bikes  glasses  pants  watches
store 1     20      NaN     30       35
store 2     15     50.0      5       10
'''

# We print the store_items DataFrame
print(store_items)

# We access rows, columns and elements using labels
print()
print('How many bikes are in each store:\n', store_items[['bikes']])
print()
print('How many bikes and pants are in each store:\n', store_items[['bikes', 'pants']])
print()
print('What items are in Store 1:\n', store_items.loc[['store 1']])
print()
print('How many bikes are in Store 2:', store_items['bikes']['store 2'])
'''
        bikes  glasses  pants  watches
store 1     20      NaN     30       35
store 2     15     50.0      5       10

How many bikes are in each store:
          bikes
store 1     20
store 2     15

How many bikes and pants are in each store:
          bikes  pants
store 1     20     30
store 2     15      5

What items are in Store 1:
          bikes  glasses  pants  watches
store 1     20      NaN     30       35

How many bikes are in Store 2: 15
'''

# We add a new column named shirts to our store_items DataFrame indicating the number of
# shirts in stock at each store. We will put 15 shirts in store 1 and 2 shirts in store 2
store_items['shirts'] = [15,2]

# We display the modified DataFrame
print(store_items)
'''
         bikes  glasses  pants  watches  shirts
store 1     20      NaN     30       35      15
store 2     15     50.0      5       10       2
'''

# We make a new column called suits by adding the number of shirts and pants
store_items['suits'] = store_items['pants'] + store_items['shirts']

# We display the modified DataFrame
print(store_items)
'''
         bikes  glasses  pants  watches  shirts  suits
store 1     20      NaN     30       35      15     45
store 2     15     50.0      5       10       2      7
'''


# We create a dictionary from a list of Python dictionaries that will number of items at the new store
new_items = [{'bikes': 20, 'pants': 30, 'watches': 35, 'glasses': 4}]

# We create new DataFrame with the new_items and provide and index labeled store 3
new_store = pd.DataFrame(new_items, index = ['store 3'])

# We display the items at the new store
print(new_store)
'''
         bikes  glasses  pants  watches
store 3     20        4     30       35
'''

store_items = store_items.append(new_store)
print(store_items)
'''
         bikes  glasses  pants  shirts  suits  watches
store 1     20      NaN     30    15.0   45.0       35
store 2     15     50.0      5     2.0    7.0       10
store 3     20      4.0     30     NaN    NaN       35
'''

# We insert a new column with label shoes right before the column with numerical index 4
store_items.insert(4, 'shoes', [8,5,0])

# we display the modified DataFrame
print(store_items)

'''
         bikes  glasses  pants  shirts  shoes  suits  watches
store 1     20      NaN     30    15.0      8   45.0       35
store 2     15     50.0      5     2.0      5    7.0       10
store 3     20      4.0     30     NaN      0    NaN       35
'''

# We remove the watches column
store_items.pop('watches')

# we display the modified DataFrame
print(store_items)
'''
         bikes  glasses  pants  shirts  shoes  suits
store 1     20      NaN     30    15.0      8   45.0
store 2     15     50.0      5     2.0      5    7.0
store 3     20      4.0     30     NaN      0    NaN
'''

# We remove the watches and shoes columns
store_items = store_items.drop(['pants', 'shoes'], axis = 1)

# we display the modified DataFrame
print(store_items)
'''
         bikes  glasses  shirts  suits
store 1     20      NaN    15.0   45.0
store 2     15     50.0     2.0    7.0
store 3     20      4.0     NaN    NaN
'''

# We remove the store 2 and store 1 rows
store_items = store_items.drop(['store 2', 'store 1'], axis = 0)

# we display the modified DataFrame
print(store_items)
'''
         bikes  glasses  shirts  suits
store 3     20      4.0     NaN    NaN
'''

# We change the column label bikes to hats
store_items = store_items.rename(columns = {'bikes': 'hats'})

# we display the modified DataFrame
print(store_items)
'''
         hats  glasses  shirts  suits
store 3    20      4.0     NaN    NaN
'''
# We change the row label from store 3 to last store
store_items = store_items.rename(index = {'store 3': 'last store'})

# we display the modified DataFrame
print(store_items)
'''
            hats  glasses  shirts  suits
last store    20      4.0     NaN    NaN
'''

# We change the row index to be the data in the pants column
store_items = store_items.set_index('suits')

# we display the modified DataFrame
print(store_items)
