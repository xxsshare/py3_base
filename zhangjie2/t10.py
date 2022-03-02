# 作者：sxx
# 日期：2022/2/15 0015 下午 5:06
# File：t10.py
# Python版本：3.7

"""
求 s = a+aa+aaa+aaaa+aa...a的值

如： n = 5   a = 3
s = 3+33+333+3333+33333
33333 = 3*10**4 + 3*10**3 + 3*10**2 + 3*10**1 + 3*10**0
"""

n = 5
a = 3
s = 0  # 下一个数
sum = 0  # 累加之和
for i in range(n):
    s += a*10**i
    print(s)
    sum += s
print(sum)

# for i in range(5):
#     print(i)


