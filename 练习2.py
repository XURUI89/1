#!/usr/bin/env python 
# -*- coding:utf-8 -*-
'''
1.我定义了一个类，可以自动弹出窗口，输入年龄
2.我用age先取数
3.我用函数property完成三步走
4.第一步是修改，第二步输出，第三步删除

问题是：一个property只能修改一个变量

'''
class person():
    def __init__(self):

        self.age=eval(input("your age:"))
        self.name=input("your name: ")

    def nameget(self):
        print("{0}".format(self._name))
    def nameset(self,name):
        self._name=name.upper()
    def namedel(self):
        print("enc")

    def personGet(self):  # 返回些啥？
        print("{0}".format(self._age))

    def personSet(self, age):  # 返回的方式是啥？
        self._age = int(age)

    def personDelete(self):  # 删除些啥？
        self._age= "noname"

    name =property(nameget,nameset,namedel,"none")
    age = property(personGet, personSet, personDelete, "说明性文字")
p1=person()  #这个是自动弹出输入框
p1.age   # 这个是调用函数
p1.name
