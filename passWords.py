#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName ：passWords.py
# @Time     ：2023/3/8 15:55
# @Author   : Pinganger


import random
import os

digital = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
letter = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
          'w', 'x', 'y', 'z']
i = 0
six_figures = str()
for i in range(6):
    six_figures = six_figures + random.choice(digital)
six_mixed = str()
i = 0
for i in range(6):
    From = random.randint(1, 2)
    if From == 1:
        six_mixed = six_mixed + random.choice(digital)
    if From == 2:
        six_mixed = six_mixed + random.choice(letter)
length = random.randint(7, 15)
random_number = str()
i = 0
for i in range(length):
    random_number = random_number + random.choice(digital)
length = random.randint(7, 15)
random_letters = str()
i = 0
for i in range(length):
    From = random.randint(1, 2)
    if From == 1:
        random_letters = random_letters + random.choice(digital)
    if From == 2:
        random_letters = random_letters + random.choice(letter)
with open('passWord.txt', 'w', encoding='UTF-8') as f:
    f.write('为您生成的六位数纯数字密码：' + six_figures)
    f.write('\n')
    f.write('为您生成的六位数混合密码：' + six_mixed)
    f.write('\n')
    f.write('为您生成的随机位数纯数字密码：' + random_number)
    f.write('\n')
    f.write('为您生成的随机位数混合密码：' + random_letters)
    f.write('\n')
print('密码生成完毕')
print('密码已保存至当前软件路径下的密码.txt文件中')
print('请不要轻易的将密码泄露给他人,谢谢您的使用')
os.system('@pause')
