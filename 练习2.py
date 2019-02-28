#!/usr/bin/env python 
# -*- coding:utf-8 -*-
'''
就是对对象进行规定，
用户输入后，计算机进行调整，输出，删除的操作
不要在里面加其他的东西，比如：input

'''


class Person():
    '''
    定义一个人
    他有属性
    年龄都是整数

    '''

    def PersonGet(self):
        return self._age  # 再搞个名字

    def PersonSet(self, age):
        self._age = int(age)

    def PersonDel(self):
        self._age = 0

    age = property(PersonGet, PersonSet, PersonDel, "输入年龄")


age = eval(input("please input your age: "))
s1 = Person()
s1.age = age
print(s1.age)