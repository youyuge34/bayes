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
    vocabSet = set([])  #创建空集合
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


def words2VecBag(vocabList, inputSet):
    """
    词袋模型
    :param vocabList:
    :param inputSet:
    :return:
    """
    ansVec = zeros(len(vocabList))
    for word in inputSet:
        if word in vocabList:
            ansVec[vocabList.index(word)] += 1
    return ansVec


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
    p0Num = ones(numWords)  # 初始化概率
    p1Num = ones(numWords)
    p0Denom = 2.0
    p1Denom = 2.0
    for i in range(numTrainDocs):
        if trainClass[i] == 1:
            p1Num += trainMatrix[i]
            p1Denom += sum(trainMatrix[i])
        else:
            p0Num += trainMatrix[i]
            p0Denom += sum(trainMatrix[i])
    p1Vect = log(p1Num / p1Denom)
    p0Vect = log(p0Num / p0Denom)
    return p0Vect, p1Vect, pAbusive


def classifyNB(vec2Classify, p0Vec, p1Vec, pClass1):
    p1 = sum(vec2Classify * p1Vec) + log(pClass1)  # element-wise mult
    p0 = sum(vec2Classify * p0Vec) + log(1.0 - pClass1)
    if p1 > p0:
        return 1
    else:
        return 0


def testingNB():
    listOPosts, listClasses = loadDataSet()
    myVocabList = createVocabList(listOPosts)
    trainMat = []
    for postinDoc in listOPosts:
        trainMat.append(words2Vec(myVocabList, postinDoc))
    p0V, p1V, pAb = trainNB0(array(trainMat), array(listClasses))
    testEntry = ['love', 'my', 'dalmation']
    thisDoc = array(words2Vec(myVocabList, testEntry))
    print testEntry, 'classified as: ', classifyNB(thisDoc, p0V, p1V, pAb)
    testEntry = ['stupid', 'garbage']
    thisDoc = array(words2Vec(myVocabList, testEntry))
    print testEntry, 'classified as: ', classifyNB(thisDoc, p0V, p1V,pAb)


## 4.6贝叶斯过滤垃圾邮件
def textParse(bigString):  # input is big string, #output is word list
    import re
    listOfTokens = re.split(r'\W*', bigString)
    return [tok.lower() for tok in listOfTokens if len(tok) > 2]


def spamTest():
    docList = [];
    classList = [];
    fullText = []
    for i in range(1, 26):
        wordList = textParse(open('email/spam/%d.txt' % i).read())
        docList.append(wordList)
        fullText.extend(wordList)
        classList.append(1)
        wordList = textParse(open('email/ham/%d.txt' % i).read())
        docList.append(wordList)
        fullText.extend(wordList)
        classList.append(0)
    vocabList = createVocabList(docList)  # create vocabulary
    trainingSet = range(50);
    testSet = []  # create test set
    for i in range(10):  # 选出10个test案例
        randIndex = int(random.uniform(0, len(trainingSet)))
        testSet.append(trainingSet[randIndex])
        del (trainingSet[randIndex])
    trainMat = [];
    trainClasses = []
    for docIndex in trainingSet:  # train the classifier (get probs) trainNB0
        trainMat.append(words2VecBag(vocabList, docList[docIndex]))
        trainClasses.append(classList[docIndex])
    p0V, p1V, pSpam = trainNB0(array(trainMat), array(trainClasses))
    errorCount = 0
    for docIndex in testSet:  # classify the remaining items
        wordVector = words2VecBag(vocabList, docList[docIndex])
        if classifyNB(array(wordVector), p0V, p1V, pSpam) != classList[docIndex]:
            errorCount += 1
            print "classification error", docList[docIndex]
    print 'the error rate is: ', float(errorCount) / len(testSet)
    # return vocabList,fullText
