# 作者：sxx
# 日期：2022/2/11 0011 下午 4:07
# File：t1.py
# Python版本：3.7

"""
水仙花数

如果一个3位数等于其各位数字的立方和，则成这个数为水仙花数。
例如：153=1^3+5^3+3^3，因此153就是一个水仙花数

问题：求1000以内的水仙花（3位数）

"""


for i in range(100,1000):
    # print(str(i))
    # print([int(j) for j in str(i)])
    # print([int(j)**3 for j in str(i)])
    if i == sum([int(j)**3 for j in str(i)]):
        print(i)

