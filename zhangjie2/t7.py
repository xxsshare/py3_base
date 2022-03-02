# 作者：sxx
# 日期：2022/2/15 0015 下午 4:12
# File：t7.py
# Python版本：3.7

"""
n 个自然数的立方和

计算公式1**3+2**3+3**3+4**3+......+n**3

实现要求：
输入：n=5
输出：225
对应公式：1**3+2**3+3**3+4**3+5**3=225

python里 三次方有两种方式
方式一：** 例如 1的三次方   1**3
方式二：pow(x, y)函数  例如 1的三次方 pow(1, 3)
"""

#  方案一
n = 5
a = 1
s = 0
while a <= n:
    s += a**3   # 相当于  s = s + a**3
    a +=1
print(s)

# 方案二  range()
n1 = int(input("请输入一个整数"))
# n1 = 5
s1 = 0
for i in range(1, n1+1):
    s1 += i**3
print(s1)

# 方案三 一行代码 列表推导式
print([j for j in range(1, 6)])
print([j**3 for j in range(1, 6)])
print(sum([j**3 for j in range(1, n1+1)]))

# 方案四  三次方也可以用pow()函数解决
print(sum([pow(i, 3) for i in range(1, n1+1)]))



