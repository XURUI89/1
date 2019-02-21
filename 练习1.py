'''
定义一个学生类，用来形容学生
'''
class Student():#定义一个空的类
    #一个空类，pass代表直接跳过
    #此处必须有
    pass

#定义一个对象
mingyue= Student()

#再定义一个类，用来描述听Python的学生
class PythonStudent():
    name = None#用none占位
    age=18
    course = "Python"


    #需要注意：
    #1.def dohomework的缩进层级
    #2.系统默认一个self参数

    def DoHomeWork(self):
        print("在做作业")

        #推荐在函数末尾使用return
        return None
#实例化一个叫月月的学生，是一个具体的人
yueyue=PythonStudent()
print(yueyue.name)
print(yueyue.age)

#注意成员函数的调用没有传递进入参数
yueyue.DoHomeWork()