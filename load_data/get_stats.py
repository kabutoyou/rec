from load_data import *

print main_data.shape

each_customer_movie_num = main_data.groupby('customer').count()['movie']
each_movie_customer_num = main_data.groupby('movie').count()['customer']

# histogram of each Number of Customer for movies and each Number of Movie
# for customers.
each_customer_movie_num.hist()
each_movie_customer_num.hist()
