# -*- coding:utf-8 -*-
# Author:Francis
import jieba
# 三种模式分词
s_list=jieba.cut("我来到北京清华大学",cut_all=True) # 默认为False
print("[全模式]:"+'/'.join(s_list))
s_list=jieba.cut("我来到北京清华大学",) # 默认是精确模式cut_all=False
print("[默认模式]:"+'/'.join(s_list))
s_list=jieba.cut_for_search("小米毕业于中科院计算所，后来在日本东京大学留学深造") # 搜索引擎模式
print("[默认模式]:"+'/'.join(s_list))

# jieba自动分词
test_string=("医疗卫生事业是强国安民的光荣事业，是为实现中国梦奠定基础的伟大事业。")
words=jieba.cut(test_string)
print('jieba默认分词效果')
print('/'.join(words))
# 加载自定义字典
jieba.load_userdict('test_string.txt')
words=jieba.cut(test_string)
print("加载自定义字典后，分词效果")
print('/'.join(words))
# 动态修改字典
t=jieba.suggest_freq(('医疗','卫生'),True)
print(t)
print('/'.join(jieba.cut(test_string, HMM=False)))
t=jieba.suggest_freq(('中国梦'),True)
print(t)
print('/'.join(jieba.cut(test_string, HMM=False)))
## 词性标注及关键字提取
import jieba.posseg as pseg
words=pseg.cut(test_string)
for word, flag in words:
    print('%s %s' % (word, flag))
