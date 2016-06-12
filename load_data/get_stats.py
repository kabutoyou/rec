from load_data import *

print userData.shape

eachCustomerMovieNum = userData.groupby('customer').count()['movie']
eachMovieCustomerNum = userData.groupby('movie').count()['customer']

# histogram of each Number of Customer for movies and each Number of Movie
# for customers.
eachCustomerMovieNum.hist()
eachMovieCustomerNum.hist()
