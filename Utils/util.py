#encoding:utf-8
import os,django

from numpy import NaN

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "MovieRecommend.settings")# project_name 项目名称
django.setup()

import pandas as pd

##############################
from recommender.models import Movies
from recommender.models import Links

def getMovieOfId(id): # from internet
    pass


############################# 建表 ，只需运行一次 #################
def movieDataToDatabase():
    movies = pd.read_csv('../dataset/movies.csv')
    for i in range(len(movies)):
        print(movies.iloc[i]['movieId'])
        movie = Movies(movieId = movies.iloc[i]['movieId'],\
                       title =  movies.iloc[i]['title'],\
                       genres = movies.iloc[i]['genres'])
        movie.save()
def LinkDataToDatabase(): ############### 待完成 ############
    links = pd.read_csv('../dataset/links.csv')
    for i in range(len(links)):
        print(links.iloc[i]['movieId'])
        link = Links(movieId = links.iloc[i]['movieId'],\
                     imdbId = links.iloc[i]['imdbId'],\
                     tmdbId = links.iloc[i]['tmdbId'] if links.iloc[i]['tmdbId']!= None else 0)
        link.save()
############################# 从数据库中获取电影信息 ##################
def getMovieInfo(id):
    res = Movies.objects.get(movieId = id)
    return res.movieId,res.title.encode('utf-8'),res.genres.encode('utf-8')

if __name__ =='__main__':
    print(getMovieInfo(1))
    # LinkDataToDatabase()