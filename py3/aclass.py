#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:jiaming
# Date: 2018/12/22 14:56
# Describe: Class & Instance


class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_score(self):
        print("%s: %d" % (self.name, self.score))


print(Student)
bart = Student('Jack', 30)
print(bart)
bart.name = 'Jason Borne'
print(bart.print_score())
