#-*- coding: utf-8 -*-
import pandas as pd
import jieba 

inputfile1 = '../jinlongyu_neg.txt'
inputfile2 = '../jinlongyu_pos.txt'
outputfile1 = '../jinlongyu_neg_cut.txt'
outputfile2 = '../jinlongyu_pos_cut.txt'

data1 = pd.read_csv(inputfile1, encoding = 'utf-8', header = None) 
data2 = pd.read_csv(inputfile2, encoding = 'utf-8', header = None)

mycut = lambda s: ' '.join(jieba.cut(s))
data1 = data1[0].apply(mycut) #广播
data2 = data2[0].apply(mycut)

data1.to_csv(outputfile1, index = False, header = False, encoding = 'utf-8') 
data2.to_csv(outputfile2, index = False, header = False, encoding = 'utf-8')
