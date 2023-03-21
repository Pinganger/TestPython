#!/usr/bin/env python
# -*- coding:utf-8 -*-
# ========================================
# @FileName ：dataType.py
# @Time     ：2023/3/19 16:30
# @Author   : Pinganger
# @Email    ：yaopinghua673@outlook.com
# @Company  ：Hua'an CO.,LTD.
# ========================================
# 数据类型
# 1、数值类型：整数、小数（浮点数）

# 数值类型的运算:
# 1.算术运算符: 加 + 减- 乘* 除/ 除法 取整 //除法取余%幂运算 **比较运算符:I
# 2.比较运算符: 大于> 小于< 大于等于:>= 小于等于<= 不等于!= 等等==

age = 28
print(5**3)
print(10*2 == 100)

# 2字符串类型:
# 字符串: 可以通过引号来表示单引号、双引号、引号 (单双都可以) :
# 以对特殊的符号进行转义字符串转义:":表示一个":表示一个n:表示换行(换行符) t:表示制表符 (了解)
# 需求: 用变量保存一个内容为: Python'class 的字符串
print("Test Python'class")
print('Test python"class')
print('Test python\"class')

aa = 'p\tython"class'
bb = 'py\tthon"class'
cc = 'pyt\thon"class'
dd = 'pyth\ton"class'
print(aa)
print(bb)
print(cc)
print(dd)
print(aa, bb, cc, dd)
ee = '''
    name = ethan
    age  = 28
    sex  = M
'''
print(ee)

ff = ""
gg = " "
hh = None
# 获取字符串长度
print("打印长度：", len(ee))
print("打印长度：", len(ff))
print("打印长度：", len(gg))
print("打印长度：", dir(hh))
