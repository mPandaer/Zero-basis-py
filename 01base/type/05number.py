# coding:utf-8

"""
    py中的类型
    1. 数字类型
        a.整型 int
        b.浮点型 float
    2. 字符串类型
    3. 布尔类型
    4. 列表类型
    5. 元组类型
    6. 字典类型
"""

# 数字类型
print("==定义整型的两种方式==")
num = int(100)  # 定义整型
num2 = 100  # 定义整型
print("num = int(100) 的类型: " + str(type(num)))
print("num2 = 100 的类型: " + str(type(num2)))

print("==定义浮点型的两种方式==")
num3 = 3.14
num4 = float(3.14)
print("num3 = 3.14 的类型: " + str(type(num3)))
print("num4 = float(3.14) 的类型: " + str(type(num4)))

print("==数字类型的常量性==")
print()
number1 = 1
number2 = 1
number3 = 1.0
number4 = 1.0
print("==整型id验证==")
print(number1, id(number1))
print(number2, id(number2))
print()
print("==浮点型id验证==")
print(number3, id(number3))
print(number4, id(number4))


