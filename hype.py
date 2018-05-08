# -*- coding:utf-8 -*-
# Author:Francis
import jieba
hyper_str='高血压疾病症状有哪些？'
s_list=jieba.cut(hyper_str,cut_all=True) # 默认为False
print("[全模式]:"+'/'.join(s_list))
s_list=jieba.cut(hyper_str,) # 默认是精确模式cut_all=False
print("[默认模式]:"+'/'.join(s_list))
s_list=jieba.cut_for_search(hyper_str) # 搜索引擎模式
print("[搜索引擎模式]:"+'/'.join(s_list))

# jieba自动分词
words=jieba.cut(hyper_str)
print('--------------jieba默认分词效果--------------')
print('/'.join(words))
# 加载自定义字典
jieba.set_dictionary('sym.txt')
words=jieba.cut(hyper_str)
print("--------------加载自定义字典后，分词效果--------------")
print('/'.join(words))

# 动态修改字典
print('------动态修改字典结果----------')
jieba.suggest_freq(('疾病症状'),True)
print('/'.join(jieba.cut(hyper_str, HMM=True)))
jieba.suggest_freq(('疾病','症状'),True)
print('/'.join(jieba.cut(hyper_str, HMM=True)))


## 词性标注及关键字提取
print('----------词性标注及关键字提取结果-----------')
import jieba.posseg as pseg
words=pseg.cut(hyper_str)
for word, flag in words:
    print('%s %s' % (word, flag))
