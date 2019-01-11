from createTree import *
from CalcshannonEnt import *

"""
函数说明:使用决策树分类

Parameters:
    inputTree - 已经生成的决策树
    featLabels - 存储选择的最优特征标签
    testVec - 测试数据列表，顺序对应最优特征标签
Returns:
    classLabel - 分类结果
"""
def classify(inputTree,featLabels,testVec):
    firstStr=next(iter(inputTree))#获取决策树结点
    secondDict=inputTree[firstStr]#下一个字典
    featIndex=featLabels.index(firstStr)
    for key in secondDict.keys():
        if testVec[featIndex]==key:
            if type(secondDict[key]).__name__=='dict':
                classLabel=classify(secondDict[key],featLabels,testVec)
            else:
                classLabel=secondDict[key]
    return classLabel

if __name__=="__main__":
    dataSet,labels=createDataSet()
    featLabels=[]
    myTree=createTree(dataSet,labels,featLabels)
    testVec=[0,1] #测试数据
    result=classify(myTree,featLabels,testVec)
    if result=='yes':
        print("放贷")
    if result=='no':
        print("不放贷")