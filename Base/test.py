#!/usr/bin/env python
# -*- coding:utf-8 -*-
# ========================================
# @FileName ：test.py
# @Time     ：2023/4/12 15:27
# @Author   : Pinganger
# @Email    ：yaopinghua673@outlook.com
# @Company  ：Hua'an CO.,LTD.
# ========================================

age = 8
age_id = id(age)
print(age_id)
print(type(age))
print(type(str(age)))

age += 1
age += 2
age += 3
age += 4
age += 5

# name = input("name:")
# print("your name is:", name)


# name = input("name:")
# sex = input("sex:")
# hometown = input("hometown:")
# mobile = input("mobile:")
# msg = f'''
# ------------------- start of {name} -------------------
# Name        :{name}
# Sex         :{sex}
# Hometown    :{hometown}
# Mobile      :{mobile}
# ------------------- end of {name} -------------------
# '''
# print(msg)
# print(name.capitalize())

# guess_age = 28
# guess = int(input("请输入你猜测的年龄:"))
# if guess_age > guess:
#     print("欧沃，猜大了！")
# elif guess_age < guess:
#     print("欧沃，猜小了！")
# else:
#     print("恭喜，你猜对了！")

salary = int(input("input your salary:"))
if salary > 100000:
    print("1公司待遇不错！")
elif salary > 50000:
    print("2公司待遇还好！")
elif salary > 30000:
    print("3公司待遇一般!")
elif salary > 10000:
    print("4公司待遇较差!")
else:
    print("5公司待遇很差!")


# eg:
# 11.2 写个匹配成绩的小程序,成绩有ABCDE5个等级，与分数的对应关系如下
# A 90-100
# B 80-89
# C 60-79
# D 40-59
# E 0-39
# 要求用户输入0-100的数字后，你能正确打印他的对应成绩等级，比如输入的是75，则打印C
score = int(input("input your score:"))
if 89 < score < 100:
    print("你当前成绩等级为A")
elif 79 < score < 90:
    print("你当前成绩等级为B")
elif 59 < score < 80:
    print("你当前成绩等级为C")
elif 39 < score < 60:
    print("你当前成绩等级为D")
elif 0 < score < 40:
    print("你当前成绩等级为E")
else:
    print("你当前成绩输入有误，分支区间为0-100")

