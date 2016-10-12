#!/usr/bin/python
# -*- coding: UTF-8 -*-


class People:
    """
    this is a sample class contains speak method.
    """
    # 定义基本属性
    name = ''
    age = 0
    # 定义私有属性,私有属性在类外部无法直接进行访问，__weight  两个
    # 下划线开头，声明该属性为私有，不能在类地外部被使用或直接访问。在类内
    # 部的方法中使用时 self.__weight
    __weight = 0

    # 定义构造方法
    def __init__(self, n, a, w):
        self.name = n
        self.age = a
        self.__weight = w

    def speak(self):
        print("%s is speaking: I am %d years old" % (self.name, self.age))


class Student(People):
    def __init__(self, n, a, w, number):
        """
        constructor
        :rtype: object
        """
        People.__init__(self, n, a, w)
        self.number = number
        self.w = w

    def speak(self):
        People.speak(self)
        print self.number

    def talk(self):
        print(
            "%s is speaking: I am %d years old, weight = %d, id number = %s" % (
                self.name, self.age, self.w, self.number))


if __name__ == '__main__':
    v = Student("asdf", 23, 243, "q5345")
    v.talk()