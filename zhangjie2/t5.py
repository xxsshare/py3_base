# 作者：sxx
# 日期：2022/2/15 0015 下午 3:23
# File：t5.py
# Python版本：3.7

"""
计算求1+2-3+4-5... ...100
"""

# 方案一
# a = 1
# s = 0
# while a <= 100:
#     if a % 2 == 1:    # 相当于if a % 2 :
#         if a == 1:
#             s += a
#         else :
#             s -= a
#     else:
#         s += a
#     a += 1
# print(s)

# 写法二

# a = 1
# s = 0
# while a <= 100:
#     if a % 2 == 0 or a == 1:    # 相当于if a % 2 :
#         s += a
#     else:
#         s -= a
#     a += 1
# print(s)
#
#
# # 一行代码  列表推导式
# print([j if j % 2 == 0 or j == 1 else -1*j for j in range(1,101)])
# print(sum([j if j % 2 == 0 or j == 1 else -1*j for j in range(1,101)]))


def func(n):
    sums = 1
    for i in range(1, n):
        if i == i:
            continue
        if i % 2 == 0:
            sums += i
        else:
            sums -= i
    return sums


print(func(10))
