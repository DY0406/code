#-*- coding: utf-8 -*-
import pandas as pd

negfile = '../jinlongyu_neg_cut.txt'
posfile = '../jinlongyu_pos_cut.txt'
stoplist = '../stoplist.txt'

neg = pd.read_csv(negfile, encoding = 'utf-8', header = None) 
pos = pd.read_csv(posfile, encoding = 'utf-8', header = None)
stop = pd.read_csv(stoplist, encoding = 'utf-8', header = None, sep = 'tipdm')

stop = [' ', ''] + list(stop[0])

neg[1] = neg[0].apply(lambda s: s.split(' ')) 
neg[2] = neg[1].apply(lambda x: [i for i in x if i not in stop]) #判断是否停用词
pos[1] = pos[0].apply(lambda s: s.split(' '))
pos[2] = pos[1].apply(lambda x: [i for i in x if i not in stop])

from gensim import corpora, models

#负面主题分析
neg_dict = corpora.Dictionary(neg[2]) #建立词典
neg_corpus = [neg_dict.doc2bow(i) for i in neg[2]] #建立语料库
neg_lda = models.LdaModel(neg_corpus, num_topics = 3, id2word = neg_dict) #LDA模型训练
for i in range(3):
  neg_lda.print_topic(i) 

#正面主题分析
pos_dict = corpora.Dictionary(pos[2])
pos_corpus = [pos_dict.doc2bow(i) for i in pos[2]]
pos_lda = models.LdaModel(pos_corpus, num_topics = 3, id2word = pos_dict)
for i in range(3):
  neg_lda.print_topic(i) #输出每个主题
