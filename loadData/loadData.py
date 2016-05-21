import numpy as np
import pandas as pd

# User Data Load
userData = pd.read_csv('/Users/junghongpark/Desktop/recommender/movieLens/ml-100k/u.data',
                       sep='\t',
                       header=None,
                       )

userData.columns = ['customer',
                    'movie',
                    'rating',
                    'time',
                    ]

# Genre Index Load
genreIndex = pd.read_csv('/Users/junghongpark/Desktop/recommender/movieLens/ml-100k/u.genre',
                         sep='|',
                         header=None,
                         )

genreIndex.columns = ['genre',
                      'index',
                      ]

# Infomation
information = pd.read_csv('/Users/junghongpark/Desktop/recommender/movieLens/ml-100k/u.info',
                          header=None,
                          )

information.columns = ['information',
                       ]

# movie Information
movieInfo = pd.read_csv('/Users/junghongpark/Desktop/recommender/movieLens/ml-100k/u.item',
                        sep='|',
                        header=None,
                        )

movieInfo.columns = ['id',
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

#user Information
userInfo = pd.read_csv('/Users/junghongpark/Desktop/recommender/movieLens/ml-100k/u.user',
                        sep='|',
                        header=None,
                        )

userInfo.columns = ['id',
                    'age',
                    'gender',
                    'occupation',
                    'zipcode'
                    ]

#occupation
occupation = pd.read_csv('/Users/junghongpark/Desktop/recommender/movieLens/ml-100k/u.occupation',
                       sep='|',
                       header=None,
                       )

occupation.columns = ['occupation',
                      ]


