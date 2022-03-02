# 作者：sxx
# 日期：2022/2/11 0011 下午 5:16
# File：t2.py
# Python版本：3.7

"""
完全数

如果一个正整数等于除它本身之外其他所有除数之和，就称之为完全数。
例如：6是完全数，因为 6 = 1+2+3；
下一个完全数是 28 = 14+7+4+2+1。

求1000以下的完全数
"""

"""
#步骤分解法
for a in range(1, 1000):
    s = []
    for i in range(1, a):
        # print(i)
        if a % i == 0:
            s.append(i)
    # print(s)
    if sum(s) == a:
        print(a)
"""
#列表推导式
for b in range(1, 1000):
    if sum([i for i in range(1, b) if b % i == 0]) == b:
        print(b)





