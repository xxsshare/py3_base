# 作者：sxx
# 日期：2022/2/15 0015 下午 4:43
# File：t9.py
# Python版本：3.7

"""
求1+2!+3!+4!+...+10!

"""
n = 10
a = 1
s = 0
for i in range(1, n+1):
    a *= i
    print("a的阶乘", a)
    s += a
print(s)

