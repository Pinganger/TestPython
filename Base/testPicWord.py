#!/usr/bin/env python
# -*- coding:utf-8 -*-
# ========================================
# @FileName ：testPicWord.py
# @Time     ：2023/4/15 16:40
# @Author   : Pinganger
# @Email    ：yaopinghua673@outlook.com
# @Company  ：Hua'an CO.,LTD.

import easyocr
import os

# 指明所有图片所在的文件夹
images = './id_card/'
# 创建ocr的reader对象，识别中英文
ocr = easyocr.Reader(['ch_sim', 'en'])
# 识别图片文字
# content = ocr.readtext(images, detail=0)
# 遍历所有图片并识别文字，切片提取有效信息
data = []
for image in os.listdir(images):
    content = ocr.readtext(f'{images}/{image}', detail=0)
    print(f"正在识别：{image}")
    name = content[0][4:]
    gender = content[1][-1]
    nation = content[2][-1]
    birth = content[-5]
    if "月" not in birth:
        birth = content[-6] + "月" + content[-5]
    if "日" not in birth:
        birth = birth[:-1] + "日"
    address = content[-4][4:] + content[-3]
    number = content[-1]
    print(f"完成识别：{image}")
    print("-" * 50)
    data.append([name, gender, nation, birth, address, number])

import pandas as pd

# 保存识别结果至Excel
df = pd.DataFrame(data, columns=["姓名", "性别", "民族", "出生", "住址", "身份证号"])
print(f"识别结果如下：")
print(df)
df.to_excel("识别结果.xlsx", index=False)