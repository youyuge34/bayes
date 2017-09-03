# encoding: utf-8
"""
@author: yousheng
@contact: 1197993367@qq.com
@site: http://youyuge.cn

@version: 1.0
@license: Apache Licence
@file: bayes.py
@time: 17/9/3 上午9:07

"""
from numpy import *


def loadDataSet():
    postingList = [['my', 'dog', 'has', 'flea', 'problems', 'help', 'please'],
                   ['maybe', 'not', 'take', 'him', 'to', 'dog', 'park', 'stupid'],
                   ['my', 'dalmation', 'is', 'so', 'cute', 'I', 'love', 'him'],
                   ['stop', 'posting', 'stupid', 'worthless', 'garbage'],
                   ['mr', 'licks', 'ate', 'my', 'steak', 'how', 'to', 'stop', 'him'],
                   ['quit', 'buying', 'worthless', 'dog', 'food', 'stupid']]
    classVec = [0, 1, 0, 1, 0, 1]  # 1 is abusive, 0 not
    return postingList, classVec


def createVocabList(dataSet):
    vocabSet = set([])  # 创建空集合
    for document in dataSet:
        vocabSet = vocabSet | set(document)
    return list(vocabSet)  # 获得元素不重复的词汇表list


def words2Vec(vocabList, inputSet):
    """
    在词汇表中的单词，是否在输入文档中出现
    :param vocabList: 词汇表
    :param inputSet: 要辨别的输入文档
    :return: 出现为1，不出现为0
    """
    ansList = [0] * len(vocabList)
    for word in inputSet:
        if word in vocabList:
            ansList[vocabList.index(word)] = 1
        else:
            print "the word: %s is not in my Vocabulary!" % word
    return ansList


def trainNB0(trainMatrix, trainClass):
    """
    朴素贝叶斯分类器训练函数
    :param trainMatrix: 文档二维矩阵
    :param trainClass: 每篇文档对应的标签向量，1或0
    :return:
    """
    numTrainDocs = len(trainMatrix)  # 训练文档数
    numWords = len(trainMatrix[0])  # 词汇表词汇数量
    pAbusive = sum(trainClass) / float(len(trainClass))  # 计算文档属于侮辱性的概率
    p0Num = zeros(numWords)  # 初始化概率
    p1Num = zeros(numWords)
    for i in range(numTrainDocs):
        if trainClass[i] == 1:
            p1Num += trainMatrix[i]
        else:
            p0Num += trainMatrix[i]
    p1Vect = p1Num / float(sum(p1Num))  # 归一化
    p0Vect = p0Num / float(sum(p0Num))
    return p0Vect, p1Vect, pAbusive
