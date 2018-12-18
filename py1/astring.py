#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:jiaming
# Date: 2018/12/17 20:16
# Describe:字符型

# 字符串：是以单引号''或者双引号""括起来的文本
# 部分字符需要转义，如 ' " \等，转移符为 \
# 制表符 \t   换行符 \n
print("Hello , I'm Jiaming, I Say \"Hi\"\\")
print('-------------------------------------')
# 换行，除了 \n 外，还可以用 '''...'''（交互命令行用这个，程序里无需...）表示多行内容，增加程序阅读性
print('Hello \n World \n')
print('-------------------------------------')
print('''Hello
This is
Jiaming''')
print('-------------------------------------')
# 字符串前加r，防止字符串转义
str = r'Hello \' \t \n Jiaming'
print(str)
print(r'''Hello,\n
World''')
