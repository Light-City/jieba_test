# -*- coding:utf-8 -*-
# Author:Francis
import jieba
test_string=("医疗卫生事业是强国安民的光荣事业，是为实现中国梦奠定基础的伟大事业。")
words=jieba.cut(test_string)
print('jieba默认分词效果')
print('/'.join(words))
# 加载自定义字典
jieba.set_dictionary('test_string.txt')
words=jieba.cut(test_string)
print("加载自定义字典后，分词效果")
print('/'.join(words))
