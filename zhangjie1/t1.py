# 作者：sxx
# 日期：2021/11/15 0015 下午 6:12
# File：t1.py
# Python版本：3.7

""""
已知 a 的值为 "hello"，b 的值为 "world"，如何交换 a 和 b 的值？
得到 a 的值为 "world"，b 的值为 "hello"

"""

# 1、中间变量法

a = "hello"
b = "world"
# temp = a
# a = b
# b = temp

# 2、python专业写法
a,b = b,a

print("a的值："+a)
print("b的值："+b)