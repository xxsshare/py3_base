# 作者：sxx
# 日期：2021/11/17 0017 下午 5:57
# File：t17.py
# Python版本：3.7

"""
统计字符串“hello, welcome to my world."中字母w出现的次数
统计单词 my 出现的次数
"""

a = "hello, welcome to my world."

print(a.count("w"))

print(a.count("my"))

#添加起始位置  没有加起始位置，默认是取的全部字符串  w位置在8和22

print(a.count("w", 6, 8))

