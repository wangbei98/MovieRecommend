#encoding:utf-8
from django.test import TestCase

# Create your tests here.
import pandas as pd
from math import sqrt
import numpy as np


# rating = pd.read_csv('../dataset/ratings.csv')
rating = pd.read_csv('/Users/bellick/MyProjects/MovieRecommend/dataset/ratings.csv')
rating = rating.iloc[:,[0,2,1]]

# rating = rating.iloc[:1000,:]

# print(rating)

user = {} # 基于用户的数据

for i in range(len(rating)):
    if rating.iloc[i]['userId'] not in user:
        user[int(rating.iloc[i]['userId'])] = {}
    user[int(rating.iloc[i]['userId'])][int(rating.iloc[i]['movieId'])] = float(rating.iloc[i]['rating'])

# print(user)
class recommender:
    # data：数据集，这里指users
    # k：表示得出最相近的k的近邻
    # metric：表示使用计算相似度的方法
    # n：表示推荐book的个数
    def __init__(self, data, k=3, metric='pearson', n=15):

        self.k = k
        self.n = n
        self.username2id = {}
        self.userid2name = {}
        self.productid2name = {}

        self.metric = metric
        if self.metric == 'pearson':
            self.fn = self.pearson
        if type(data).__name__ == 'dict':
            self.data = data
    def convertProductID2name(self, id):

        if id in self.productid2name:
            return self.productid2name[id]
        else:
            return id

    # 定义的计算相似度的公式，用的是皮尔逊相关系数计算方法
    def pearson(self, rating1, rating2):
        sum_xy = 0
        sum_x = 0
        sum_y = 0
        sum_x2 = 0
        sum_y2 = 0
        n = 0
        for key in rating1:
            if key in rating2:
                n += 1
                x = rating1[key]
                y = rating2[key]
                sum_xy += x * y
                sum_x += x
                sum_y += y
                sum_x2 += pow(x, 2)
                sum_y2 += pow(y, 2)
        if n == 0:
            return 0

        # 皮尔逊相关系数计算公式
        denominator = sqrt(sum_x2 - pow(sum_x, 2) / n) * sqrt(sum_y2 - pow(sum_y, 2) / n)
        if denominator == 0:
            return 0
        else:
            return (sum_xy - (sum_x * sum_y) / n) / denominator

    # 计算其他用户 到本用户的距离 并排序
    def computeNearestNeighbor(self, id):
        distances = []
        for instance in self.data:
            if instance != id:
                distance = self.fn(self.data[id], self.data[instance])
                distances.append((instance, distance))

        distances.sort(key=lambda artistTuple: artistTuple[1], reverse=True)
        return distances

    # 推荐算法的主体函数
    def recommend(self, id):
        # 定义一个字典，用来存储推荐的电影单和分数
        recommendations = {}
        # 计算出user与所有其他用户的相似度，返回一个list
        nearest = self.computeNearestNeighbor(id)
        #         print nearest

        userRatings = self.data[id]
        #         print userRatings
        totalDistance = 0.0
        # 得住最近的k个近邻的总距离
        for i in range(self.k):
            totalDistance += nearest[i][1]
        if totalDistance == 0.0:
            totalDistance = 1.0

        # 将与user最相近的k个人中user没有看过的书推荐给user
        for i in range(self.k):

            # 第i个人的与user的相似度，转换到[0,1]之间
            weight = nearest[i][1] / totalDistance

            # 第i个人的id
            id = nearest[i][0]

            # 第i个用户看过的书和相应的打分
            neighborRatings = self.data[id]

            for artist in neighborRatings:
                if not artist in userRatings:
                    if artist not in recommendations:# 本电影在不在推荐单内，则添加进去，并设置权重为 此用户对这部电影的评分* 此用户的权重
                        recommendations[artist] = (neighborRatings[artist] * weight)
                    else: # 本电影已经在推荐单内，则增加它的权重
                        recommendations[artist] = (recommendations[artist] + neighborRatings[artist] * weight)

        recommendations = list(recommendations.items())

        # 按照每部电影的权重排序
        recommendations.sort(key=lambda artistTuple: artistTuple[1], reverse=True)

        #         print recommendations[:self.n],"-------"
        return recommendations[:self.n]


def recommend(id):
    moviei_d_list = []
    r = recommender(user)
    k = r.recommend(id)
    for i in range(len(k)):
        moviei_d_list.append(k[i][0])
    return moviei_d_list


##############################
def getMovieOfId(id):
    pass


#############################
def movieDataToDatabase():
    pass

#############################
def getMovieInfo(id):
    pass



if __name__ =='__main__':
    print(recommend(1))