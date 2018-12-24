import pandas as pd
import numpy as np

# Since we will be working with ratings, we will set the precision of our 
# dataframes to one decimal place.
pd.set_option('precision', 1)

# Create a Pandas DataFrame that contains the ratings some users have given to a
# series of books. The ratings given are in the range from 1 to 5, with 5 being
# the best score. The names of the books, the authors, and the ratings of each user
# are given below:

books = pd.Series(data = ['Great Expectations', 'Of Mice and Men', 'Romeo and Juliet', 'The Time Machine', 'Alice in Wonderland' ])
authors = pd.Series(data = ['Charles Dickens', 'John Steinbeck', 'William Shakespeare', ' H. G. Wells', 'Lewis Carroll' ])

user_1 = pd.Series(data = [3.2, np.nan ,2.5])
user_2 = pd.Series(data = [5., 1.3, 4.0, 3.8])
user_3 = pd.Series(data = [2.0, 2.3, np.nan, 4])
user_4 = pd.Series(data = [4, 3.5, 4, 5, 4.2])

# Users that have np.nan values means that the user has not yet rated that book.
# Use the data above to create a Pandas DataFrame that has the following column
# labels: 'Author', 'Book Title', 'User 1', 'User 2', 'User 3', 'User 4'. Let Pandas
# automatically assign numerical row indices to the DataFrame. 

# Create a dictionary with the data given above
dat = {"Authors":authors,"Book title":books,"User 1":user_1,"User 2":user_2,"User 3":user_3,"User 4":user_4}

# Use the dictionary to create a Pandas DataFrame
book_ratings = pd.DataFrame(dat)

# If you created the dictionary correctly you should have a Pandas DataFrame
# that has column labels: 'Author', 'Book Title', 'User 1', 'User 2', 'User 3',
# 'User 4' and row indices 0 through 4.
print(book_ratings)
'''
               Authors           Book title  User 1  User 2  User 3  User 4
0      Charles Dickens   Great Expectations     3.2     5.0     2.0     4.0
1       John Steinbeck      Of Mice and Men     NaN     1.3     2.3     3.5
2  William Shakespeare     Romeo and Juliet     2.5     4.0     NaN     4.0
3          H. G. Wells     The Time Machine     NaN     3.8     4.0     5.0
4        Lewis Carroll  Alice in Wonderland     NaN     NaN     NaN     4.2
'''

# Now replace all the NaN values in your DataFrame with the average rating in
# each column. Replace the NaN values in place. HINT: you can use the fillna()
# function with the keyword inplace = True, to do this. Write your code below:

book_ratings.fillna(book_ratings.mean(), inplace = True)
print(book_ratings)

'''
               Authors           Book title  User 1  User 2  User 3  User 4
0      Charles Dickens   Great Expectations     3.2     5.0     2.0     4.0
1       John Steinbeck      Of Mice and Men     2.9     1.3     2.3     3.5
2  William Shakespeare     Romeo and Juliet     2.5     4.0     2.8     4.0
3          H. G. Wells     The Time Machine     2.9     3.8     4.0     5.0
4        Lewis Carroll  Alice in Wonderland     2.9     3.5     2.8     4.2
'''