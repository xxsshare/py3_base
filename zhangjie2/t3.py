# 作者：sxx
# 日期：2022/2/11 0011 下午 5:49
# File：t3.py
# Python版本：3.7

"""
求数字1+2+3+4+5+。。。。。。+100的和
"""
"""
s = []
for i in range(1,101):
    s.append(i)
print(s)
print(sum(s))
"""


# 列表生成式  一行代码解决
print(sum([i for i in range(1, 101)]))


a = 1
s = 0
while a <= 100:
    s += a            # 等价s = s + a
    a += 1            # 自增+1（类似于i++） 等价a = a + 1
print(s)


s1 = 0
for i in range(1, 101):
    s1 += i
print(s1)


