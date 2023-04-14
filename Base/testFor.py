#!/usr/bin/env python
# -*- coding:utf-8 -*-
# ========================================
# @FileName ：testFor.py
# @Time     ：2023/4/14 9:43
# @Author   : Pinganger
# @Email    ：yaopinghua673@outlook.com
# @Company  ：Hua'an CO.,LTD.
# ========================================

# ====================
# for x in range(10):
#     print(x)
# print(list(range(x)))
# ====================
# a = 3
# guess_age = 28
# for b in range(a):
#     guess = int(input("请输入你猜测的年龄:"))
#     if guess > guess_age:
#         print("欧沃，猜大了！")
#     elif guess < guess_age:
#         print("欧沃，猜小了！")
#     else:
#         exit("恭喜，你猜对了！")
# ====================
# for i in range(100):
#     if i % 2 == 0:
#         print(f"偶数是：", list({i}))
#     else:
#         print(f"奇熟是：", list({i}))
# ====================
# floor = 5
# room = 32
# for i in range(1, floor):
#     print(f"-----------当前楼层F{i}-----------------")
#     for j in range(1, room):
#         print(f"当前房间号L{i}0{j}")
# ====================
# floor = 5
# room = 6
# for i in range(1, floor):
#     print(f"-----------当前楼层F{i}-----------------")
#     if i == 3:
#         print(f"L{i}0{j}测试打印情况")
#         continue
#     for j in range(1, room):
#         if i == 4:
#             print(f"L{i}0{j}测试打印情况")
#             continue
#         if i == 2 and j == 4:
#             print(f"当前房间号L{i}0{j}测试不打印")
#             break
#         print(f"当前房间号L{i}0{j}")
# ====================
# for i in range(10):
#     if i <= 5:
#         print("*"*i)
#     else:
#         print((10-i)*"*")
# ====================
# count = 0
# while True:
#     count += 1
#     print(f"这是Deal Toop：", count)
# ====================
# count = 0
# while count < 200000:
#     count += 1
#     print(f"这是Deal Toop：", count)
# ====================
# 摇号小程序
# 需求
# 1.允许用户最多选3次
# 2.每次放出20个车牌供用户选择
# 3.京[A-Z]-[xxxxx],可以是数字和字母在组合
import random
import string

choose = 3
word = string.ascii_uppercase
plate = random.sample(word, 2)
print("".join(plate))
print(string.digits)

# import re
#
# re_str = '([京津沪渝冀豫云辽黑湘皖鲁新苏浙赣鄂桂甘晋蒙陕吉闽贵粤青藏川宁琼使领]' \
#          '{1}[A-Z]{1}(([A-HJ-NP-Z0-9]{5}[DF]{1})|' \
#          '([DF]{1}[A-HJ-NP-Z0-9]{5})))|' \
#          '([京津沪渝冀豫云辽黑湘皖鲁新苏浙赣鄂桂甘晋蒙陕吉闽贵粤青藏川宁琼使领]{1}' \
#          '[A-Z]{1}[A-HJ-NP-Z0-9]{4}[A-HJ-NP-Z0-9挂学警港澳]{1})'
# strs = '苏A12345WDD晋ADAAjgaADAQQQWW京B1234456F'
# ss = re.finditer(re_str, strs)
# for i in ss:
#     print(i.group())

# 定义用户选择次数
count = 0
# 定义车牌身份库
province = '京津沪渝冀豫云辽黑湘皖鲁新苏浙赣鄂桂甘晋蒙陕吉闽贵粤青藏川宁琼使领'
# 字符串转列表随机取一个
pro = random.choice(list(province))
print(f"您选择的车牌对应省份：", pro)
# 开启3次选牌模式
while count < 3:
    car_nums = []
    for i in range(20):
        # 生成车牌前一个字母（大写）
        a = random.choice(string.ascii_uppercase)
        # 生成车牌后5个值（数字与字母-大写）
        b = "".join(random.sample(string.ascii_uppercase + string.digits, 5))
        # 打印车牌号
        nums = f"{pro}{a}-{b}"
        # 生成车牌库（追加）
        car_nums.append(nums)
        print(f"随机生成车牌号：", i+1, nums)

    print(f"当期生成车牌库：", car_nums)
    choice = input("请输入（选择）你喜欢的车牌号：").strip()  # strip()去除空格
    if choice in car_nums:
        print("恭喜你选择新的车牌：", choice)
        exit()
    else:
        print("你输入的车牌不在清单内，请重新选择")
        count += 1
