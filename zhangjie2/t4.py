# 作者：sxx
# 日期：2022/2/15 0015 下午 2:38
# File：t4.py
# Python版本：3.7

"""
求数字1-2+3-4+5-...-100之和

思路：偶数-，奇数+

"""

# 方案一

a = 1
s = 0
# while a <= 100:
#     if a % 2 == 1:    #相当于if a % 2 :
#         s += a
#     else:
#         s -= a
#     a += 1
# print(s)

while a <= 100:
    if a % 2 == 0:
        s -= a
    else:
        s += a
    a += 1
print(s)

# 方案二：一行代码  列表推导式
print([j if j % 2 else -1*j for j in range(1, 101)])  # 这个列表推导式，为啥if else要放到前面
print(sum([j if j % 2 else -1*j for j in range(1, 101)]))







