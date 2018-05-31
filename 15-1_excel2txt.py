#-*- coding: utf-8 -*-
import pandas as pd

inputfile = '../all.csv' 
outputfile = '../jinlongyu.txt' 
data = pd.read_csv(inputfile, encoding = 'utf-8')
data = data[[u'评论']][data[u'品牌'] == u'金龙鱼']
data.to_csv(outputfile, index = False, header = False, encoding = 'utf-8')
