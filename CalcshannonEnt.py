from math import log
def createDataSet():
    dataSet=[[0, 0, 0, 0, 'no'],         #数据集
            [0, 0, 0, 1, 'no'],
            [0, 1, 0, 1, 'yes'],
            [0, 1, 1, 0, 'yes'],
            [0, 0, 0, 0, 'no'],
            [1, 0, 0, 0, 'no'],
            [1, 0, 0, 1, 'no'],
            [1, 1, 1, 1, 'yes'],
            [1, 0, 1, 2, 'yes'],
            [1, 0, 1, 2, 'yes'],
            [2, 0, 1, 2, 'yes'],
            [2, 0, 1, 1, 'yes'],
            [2, 1, 0, 1, 'yes'],
            [2, 1, 0, 2, 'yes'],
            [2, 0, 0, 0, 'no']]
    labels=['不放贷','放贷']
    return dataSet,labels
def calcshannonEnt(dataSet):
        numEntries=len(dataSet)
        labelCounts={}
        for featVec in dataSet:
                currentLabel=featVec[-1]
                if currentLabel not in labelCounts.keys(): #如果标签(Label)没有放入统计次数的字典,添加进去
                        labelCounts[currentLabel]=0
                labelCounts[currentLabel]+=1#Label计数
        shannonEnt=0.0
        for key in labelCounts:
                prob=float(labelCounts[key]/numEntries)
                shannonEnt-=prob*log(prob,2)
        return shannonEnt

'''
arameters:
    dataSet - 待划分的数据集
    axis - 划分数据集的特征
    value - 需要返回的特征的值
'''
def splitDataSet(dataSet,axis,value):#按照给定特征划分数据集
        retDataSet=[]
        for featVec in dataSet:
                if featVec[axis]==value:
                        reducedFecVec=featVec[:axis]#去掉axis特征
                        reducedFecVec.extend(featVec[axis+1:])#将符合条件的添加到返回的数据集
                        retDataSet.append(reducedFecVec)
        return retDataSet #返回划分后的数据集

def chooseBestFeatureToSplit(dataSet):
        numFeatures=len(dataSet[0])-1#特征数量
        baseEntropy=calcshannonEnt(dataSet) #计算数据集的香农熵
        bestInfoGain=0.0#信息增益
        bestFeature=-1 #最优特征的索引值
        for i in range(numFeatures):
                featList=[example[i] for example in dataSet]
                uniqueVals=set(featList)
                newEntroy=0.0 #经验条件熵
                for value in uniqueVals: #计算信息增益
                        subDataSet=splitDataSet(dataSet,i,value)#subDataSet划分后的子集
                        prob=len(subDataSet)/float(len(dataSet)) #计算子集的概率
                        newEntroy+=prob*calcshannonEnt(subDataSet)#根据公式计算经验条件熵
                infoGain=baseEntropy-newEntroy
                print("第%d个特征的增益为%.3f"%(i,infoGain))
                if (infoGain>bestInfoGain): #计算信息增益
                        bestInfoGain=infoGain #更新信息增益，找到最大的信息增益
                        bestFeature=i #记录信息增益最大的特征的索引值
        return bestFeature #返回信息增益最大的特征的索引值




if __name__=="__main__":
        dataSet,features=createDataSet()
        print('最优索引值:'+str(chooseBestFeatureToSplit(dataSet)))
        #print(dataSet)
        #print(calcshannonEnt(dataSet))
