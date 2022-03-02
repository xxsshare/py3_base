# 作者：sxx
# 日期：2022/2/15 0015 下午 4:33
# File：t8.py
# Python版本：3.7

"""
阶乘10！

阶乘的意思：10！=10*9*8*7*6*5*4*3*2*1

求10！

"""
# 方案一 for  range()函数
s = 1
n = 10
for i in range(1, n+1):
    s = s*i
print(s)

# 方案二 while
n = 10
s = 1
while n >=1:
    s *= n   # 相当于 s = s*n
    n -= 1   # 相当于 n = n-1
print(s)


