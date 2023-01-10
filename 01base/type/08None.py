# coding=utf-8

"""
    空类型
        空代表没有类型的类型或者说不知道具体类型的一种符号表示，类似于未知
        一般用于开始不知道具体的类型，但是又要定义变量的情况,定义变量就必须要赋值，但是不知道具体的类型，所以就先赋值为None
"""
print("==空类型==")
username = None
password = None
print("username = None", id(username), type(username))
print("password = None", id(password), type(password))
print("==空类型的常量性==")
print("id(username) == id(password)", id(username) == id(password))
