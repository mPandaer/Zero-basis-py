# coding=utf-8

"""
    元组
        不可改变的列表
"""

print("==创建元组的两种方式==")
tuple1 = (1, 2, 3)
tuple2 = tuple((1, 2, 3))
print(tuple1, id(tuple1), type(tuple1))
print(tuple2, id(tuple2), type(tuple2))
print()

print("==元组的常量性==")
print("id(tuple1) == id(tuple2)", id(tuple1) == id(tuple2))
print()

print("==元组中能存放的类型==")
tuple1 = (1, 2, 3)
tuple2 = ("username",)  # 只有一个元素的元组记得加英文逗号
tuple3 = (True, False, True, False)
tuple4 = (None,)
tuple5 = ([1, 3], [1])
tuple6 = ([1, 3], [1], "password", None, True, False, 1)
print(tuple1)
print(tuple2)
print(tuple3)
print(tuple4)
print(tuple5)
print()

print("==成员运算符==")
res1 = 1 in tuple1
res2 = 1 not in tuple1
print("res1 = 1 in tuple1", res1)
print("res2 = 1 not in tuple1", res2)
print()
print("max&min函数")
print(tuple1)
print("max(tuple1)", max(tuple1))
print("min(tuple1)", min(tuple1))

# 和列表一样混合类型不能比较
# min(tuple6)
