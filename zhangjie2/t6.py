# 作者：sxx
# 日期：2022/2/15 0015 下午 3:44
# File：t6.py
# Python版本：3.7

"""
定义一个函数：计算1-n之间的所有5的倍数之和，默认计算1-100 （n是一个整数）

"""

# n = input("请输入一个整数：")
# s = 0
# for i in range(1, int(n)):
#     if i % 5 == 0:
#         s += i
# print(s)

# a = 1
# n = 100
# s = 0
# while a <= n:
#     if a % 5 == 0:
#         s += a
#     a +=1
# print(s)
#
#
# # 一行代码  列表推导式
# print([j for j in range(1, 101) if j % 5 == 0])
# print(sum([j for j in range(1, 101) if j % 5 == 0]))


# 定义一个函数

def fun5(n=100):
    """计算1-n之间的所有5的倍数之和 """
    return sum([j for j in range(1, n+1) if j % 5 == 0])


if __name__ == '__main__':
    fun5()








