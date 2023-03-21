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

name = input('请输入姓名：')
age = input('请输入年龄：')
sex = input('请输入性别：')
demo1 = 80
demo2 = 70
print("---------------------")
print("你的姓名是：", name)
print("你的年龄是：", age)
print("你的性别是：", sex)
print("---------------------")

# 字符串格式化：字符串拼接（+）、format、传统百分号%
# 1、字符串拼接+
desc1 = "你的信息1是:"+"姓名" + name + "年龄" + sex + "性别" + age
print("你的信息1是:"+"姓名" + name + "年龄" + sex + "性别" + age)
print(desc1)
# 2、格式化format函数，采用{}
desc2 = "你的信息2:姓名是{},年龄{}岁,性别为{}"
print(desc2.format(name, age, sex))
desc2_0 = "你的信息2_0:姓名是{},年龄{}岁,性别为{},存款为{:.3f},负债为{:.0f}"
print(desc2_0.format(name, age, sex, 987654321.123456, -987654321.123456))
# 3、传统百分号%s %var
# %s 表示一个字符串占位符(后面填任意类型的数据都可以)
# %f 表示一个整数占位符(后面只能填数值类型的数据，会转换为整数)
# %f 表示一个浮点数占位(后面只能填数值类型的数据，为转换为小数) bool int float
desc3 = "你的信息3:姓名是%s,年龄%s岁,性别为%s" % (name, age, sex)
print(desc3)
# 4、字符串F的表达式（f/F都可以）
desc4 = F'你的信息4:姓名是{name},年龄{age}岁,性别为{sex}'
print(desc4)
# 5、格式化百分比显示
desc5 = '5接口自动化用例通过率为{:.2f}'.format(98.67832)
desc5_0 = '5_0接口自动化用例通过率为{:.2f}'.format(demo2/demo1)
print(desc5)
print(desc5_0)
# 6、格式化长度
print("你的信息：姓名是{:^8},年龄为{:^2},性别是{}".format('Zhangsan', 28, '男'))
print("你的信息：姓名是{:^8},年龄为{:^2},性别是{}".format('lisi', 36, '男'))
print("你的信息：姓名是{:^8},年龄为{:^2},性别是{}".format('Wangwu', 100, '女'))
