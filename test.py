# encoding: utf-8
"""
@author: yousheng
@contact: 1197993367@qq.com
@site: http://youyuge.cn

@version: 1.0
@license: Apache Licence
@file: test.py
@time: 17/9/3 上午9:28

"""
import bayes

def run():
    print 'begin--->run()'
    postingList,classVec = bayes.loadDataSet()
    myVocabList = bayes.createVocabList(postingList)
    print myVocabList
    print bayes.words2Vec(myVocabList,postingList[0])


if __name__ == '__main__':
    run()