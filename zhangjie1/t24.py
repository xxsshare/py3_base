# 作者：sxx
# 日期：2022/2/11 0011 下午 3:11
# File：t24.py
# Python版本：3.7

"""
输入一个正整数，判断是几位数：

给一个不多于5位的正整数，要求：
一、求它是几位数，
二、逆序打印出各位数字54321

"""

# a = 12345
a = input("请输入一个不多于5位的正整数：")
# print(a)
# print(len(a))    #object of type 'int' has no len()
print(str(a))
print(len(str(a)))  #len() 求字符串的长度

print("a 的位数：%s" % len(str(a)))
print("a 逆序打印 %s" % str(a)[::-1])








