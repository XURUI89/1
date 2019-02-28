#!/usr/bin/env python 
# -*- coding:utf-8 -*-
class student():
    def __init__(self, name):
        self._name = name

    def __gt__(self, obj):  # 同类比较
        print("haha,{0}比{1}大?".format(self._name,obj._name))
        return self._name > obj._name


stu1 = student("one")
stu2 = student("two")

print(stu1 > stu2)