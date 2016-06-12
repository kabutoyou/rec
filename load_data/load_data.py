import pandas as pd

# Main Data Load
main_data = pd.read_csv(
    '../data/recommender/movieLens/ml-100k/u.data',
    sep='\t',
    header=None,
)

main_data.columns = ['customer',
                     'movie',
                     'rating',
                     'time',
                     ]

# Genre Index Load
genre_index = pd.read_csv(
    '../data/recommender/movieLens/ml-100k/u.genre',
    sep='|',
    header=None,
)

genre_index.columns = ['genre',
                       'index',
                       ]

# Infomation
information = pd.read_csv(
    '../data/recommender/movieLens/ml-100k/u.info',
    header=None,
)

information.columns = ['information',
                       ]

# Movie Information
movie_info = pd.read_csv(
    '../data/recommender/movieLens/ml-100k/u.item',
    sep='|',
    header=None,
)

movie_info.columns = ['id',
                      'title',
                      'release_date',
                      'video_release',
                      'Imdb_url',
                      'Action',
                      'Adventure',
                      'Animation',
                      'Children\'s',
                      'Comedy',
                      'Crime',
                      'Documentary',
                      'Drama',
                      'Fantasy',
                      'Film-Noir',
                      'Horror',
                      'Musical',
                      'Mystery',
                      'Romance',
                      'Sci-Fi',
                      'Thriller',
                      'War',
                      'Western',
                      ]

# user Information
user_info = pd.read_csv(
    '../data/recommender/movieLens/ml-100k/u.user',
    sep='|',
    header=None,
)

user_info.columns = ['id',
                     'age',
                     'gender',
                     'occupation',
                     'zipcode'
                     ]

# occupation
occupation = pd.read_csv(
    '../data/recommender/movieLens/ml-100k/u.occupation',
    sep='|',
    header=None,
)

occupation.columns = ['occupation',
                      ]
