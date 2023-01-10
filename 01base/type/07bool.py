# coding=utf-8

"""
    布尔类型
        简单的理解就是真假类型 布尔类型来自于一个学科逻辑数学
        主要用于条件判断中（后面会详细讲解）
"""
print("==定义布尔类型的两种方式==")
bool1 = True
bool2 = bool(True)
print("bool1 = True", id(bool1), type(bool1))
print("bool2 = bool(True)", id(bool2), type(bool2))
print("==布尔类型的常量性==")
print("id(bool1) == id(bool2)", id(bool1) == id(bool2))
