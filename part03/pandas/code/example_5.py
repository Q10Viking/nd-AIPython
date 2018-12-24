# We import Pandas as pd into Python
import pandas as pd

# We create a dictionary of Pandas Series 
items = {'Bob' : pd.Series(data = [245, 25, 55], index = ['bike', 'pants', 'watch']),
         'Alice' : pd.Series(data = [40, 110, 500, 45], index = ['book', 'glasses', 'bike', 'pants'])}

# We print the type of items to see that it is a dictionary
print(type(items))
'''
<class 'dict'>
'''
# We create a Pandas DataFrame by passing it a dictionary of Pandas Series
shopping_carts = pd.DataFrame(items)

# We display the DataFrame
print(shopping_carts)
'''
           Bob  Alice
bike     245.0  500.0
book       NaN   40.0
glasses    NaN  110.0
pants     25.0   45.0
watch     55.0    NaN
'''


# We create a dictionary of Pandas Series without indexes
data = {'Bob' : pd.Series([245, 25, 55]),
        'Alice' : pd.Series([40, 110, 500, 45])}

# We create a DataFrame
df = pd.DataFrame(data)

# We display the DataFrame
print(df)
'''
     Bob  Alice
0  245.0     40
1   25.0    110
2   55.0    500
3    NaN     45
'''

# We Create a DataFrame that only has Bob's data
bob_shopping_cart = pd.DataFrame(items, columns=['Bob'])

# We display bob_shopping_cart
print(bob_shopping_cart)
'''
       Bob
bike   245
pants   25
watch   55
'''