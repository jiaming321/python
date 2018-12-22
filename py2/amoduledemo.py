#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:jiaming
# Date: 2018/12/22 14:27
# Describe: Module Demo

# Fibonacci Numbers Modules


def fib1(n):
    a, b = 0, 1
    while b < n:
        print(b, end=' ')
        a, b = b, a+b
    print()


def fib2(n):
    result = []
    a, b = 0, 1
    while b < n:
        result.append(b)
        a, b = b, a+b
    return result


