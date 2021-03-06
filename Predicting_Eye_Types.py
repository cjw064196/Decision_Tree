#from sklearn import tree
import pandas as pd

if __name__=='__main__':
    with open('lenses.txt','r') as fr:
        lenses=[inst.strip().split('\t') for inst in fr.readlines()]
    lenses_target=[] #提取每组数据的类别，保存在列表里
    for each in lenses:
        lenses_target.append(each[-1])
    lensesLabels=['age','symptom','astigmatic','tearRate']
    lenses_list=[]#保存lenses数据的临时列表
    lenses_dict={}#保存lenses数据的字典，用于生成pandas
    for each_label in lensesLabels:#提取信息，生成字典
        for each in lenses:
            lenses_list.append(each[lensesLabels.index(each_label)])
        lenses_dict[each_label]=lenses_list
        lenses_list=[]
    print(lenses_dict)#打印字典信息
    lenses_pd=pd.DataFrame(lenses_dict) #生成pandas.DataFrame
    print(lenses_pd)