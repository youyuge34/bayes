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
    postingList=[['my', 'dog', 'has', 'flea', 'problems', 'help', 'please'],
                 ['maybe', 'not', 'take', 'him', 'to', 'dog', 'park', 'stupid'],
                 ['my', 'dalmation', 'is', 'so', 'cute', 'I', 'love', 'him'],
                 ['stop', 'posting', 'stupid', 'worthless', 'garbage'],
                 ['mr', 'licks', 'ate', 'my', 'steak', 'how', 'to', 'stop', 'him'],
                 ['quit', 'buying', 'worthless', 'dog', 'food', 'stupid']]
    classVec = [0,1,0,1,0,1]    #1 is abusive, 0 not
    return postingList,classVec

def createVocabList(dataSet):
    vocabSet = set([])  #创建空集合
    for document in dataSet:
        vocabSet = vocabSet | set(document)
    return list(vocabSet)   #获得元素不重复的词汇表list


def words2Vec(vocabList,inputSet):
    """
    在词汇表中的单词，是否在输入文档中出现
    :param vocabList: 词汇表
    :param inputSet: 要辨别的输入文档
    :return: 出现为1，不出现为0
    """
    ansList = [0]*len(vocabList)
    for word in inputSet:
        if word in vocabList:
            ansList[vocabList.index(word)] = 1
        else: print "the word: %s is not in my Vocabulary!" % word
    return ansList



