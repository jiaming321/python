#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Author:jiaming
# Date: 2018/12/19 22:22
# Describe: DataType -> List

# 定义和赋值

list1 = ['a', 'b', 'c']
list2 = []
print(list1)

nums = range(1, 10)
print(nums)
for x in nums:
    print(x)

# python list 可以存放不同类型的数据
list3 = [1, 2, 'ab', True, ['a', 'b', 'c']]
print(list3)

# 列式推导

resultList = []

for num in nums:
    resultList.append(num ** 2)

print('resultList =', resultList)

# [表达式 for 变量 in 列表]
resultList1 = [num ** 2 for num in nums]
print('resultList1 =', resultList1)

# [表达式 for 变量 in 列表 if 表达式]
resultList2 = [num ** 2 for num in nums if num % 2 != 0]
print('resultList2 =', resultList2)

# len()
print('len(list1) =', len(list1))

# 将一个元素添加到列表结尾 list.append(x)
# 会修改原数组
list1.append(11)
print('list1 =', list1)
# list1[len(list1):] = 12   TypeError: can only assign an iterable
list1[len(list1):] = [12]
print('list1 =', list1)

# 将特定列表的元素添加到另一个列表中 list.extend(L)   同list[len(list):] = L
list3 = ['a', 'b', 'c']
list1.extend(list3)
print('list1 =', list1)
list1[len(list1):] = [13, 14]
print('list1 =', list1)
