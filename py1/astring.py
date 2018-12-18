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

# 字符编码
# 字符编码和字符转换
print('-------------------------------------')
print(ord('A'))
print(chr(25991))
# print('\u4e2d\u6587')

# 字符串和字节类型数据 bytes 转换
# bytes类型的数据以 b为前缀的单引号或者双引号表示
print('-------------------------------------')
ss = b'ABC'
print(ss)

# encode() 指定字符集编码（为字节） 和decode() 指定解码字符集（为字符）
str = 'ABCD'
print(str.encode('ascii'))
str = '你好啊'
print(str.encode('utf-8'))

strbyte = b'\xe4\xbd\xa0\xe5\xa5\xbd\xe5\x95\x8a'
print(strbyte.decode('utf-8'))

# len() 长度计算
# print(len(12))      object of type 'int' has no len()
print(len('ABC')) # 计算字符串长度
print(len('你好啊'.encode('utf-8'))) # 计算字节长度

# -*- coding:utf-8 -*- 告诉python解释器按UTF-8编码读取源码
# windows系统保存源码选择 UTF-8 without BOM

# 格式化 python字符串格式化和c语言一致。
# %[(name)][flags][width].[precision]typecode
# []表示可选
# (name) ：指定key值
# flags ：+ 右对齐，正数前加正号，负数前加负号； - 左对齐，正数无符号，负数加负号； 空格，右对齐，正数加空格，负数加负号； 0，右对齐，正数无符号，负数加负号，0填充空白。
# width ：占位宽度
# .precision ：小数精度
# typecode ：s 字符   d 整数  f 浮点数
print('-------------------------------------')
print('hello %s, I\'m %d and My height is %.2f m'%('Jiaming', 20, 1.75123))
print('hello %(name)s, I\'m %(age)d and My height is %(height)05.2f m'%{'name': 'Jiaming', 'age': 20, 'height': 1.75123})

# format
# [[fill]align][sign][#][0][,][.precision][type]  用 : 代替 %
print('-------------------------------------')
print('----{:*^20s}----'.format('welcome'))
print('My name is {name:s}, I\'m {age:d} now and My Height is {height:,.2f}'.format(name='Jiaming', age=21, height=1111.987))

