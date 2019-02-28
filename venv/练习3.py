#!/usr/bin/env python 
# -*- coding:utf-8 -*-
class person():
    def personGet(self):  # 返回些啥？
        return self._name * 2

    def personSet(self, name):  # 返回的方式是啥？
        self._name = name.upper()

    def personDelete(self):  # 删除些啥？
        self._name = "noname"

    name = property(personGet, personSet, personDelete, "说明性文字")
p1=person()
p1.name="TuLing"
print(p1.name)