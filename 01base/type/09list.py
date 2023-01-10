# coding=utf-8

"""
    列表类型
        多个数据聚合到一起
"""
print("==定义列表的两种方式==")
list1 = [1, 2, 3]
list2 = list([1, 2, 3])
print(list1, id(list1), type(list1))
print(list2, id(list2), type(list2))

print("==列表中可以存放的数据类型==")
list1 = [1, 2, 3]
list2 = ["username", "password", "age"]
list3 = [True, False, True, False]
list4 = [None, None, None]
list5 = [1, "username", True, False, None]

print("纯数字类型 list1 = [1, 2, 3]", list1)
print('纯字符串类型 list2 = ["username", "password", "age"],', list2)
print("纯布尔类型 list3 = [True, False, True, False],", list3)
print("纯空类型 list4 = [None, None, None],", list4)
print('混合类型 list5 = [1, "username", True, False, None],', list5)

print("==成员运算符==")
res = 1 in list5
print("res = 1 in list5", res)
print("==max&min函数==")
res1 = max(list1)
res2 = min(list1)
print("list1", list1)
print("res1 = max(list1)", res1)
print("res2 = min(list1)", res2)
print("比较操作只能发生在同类型中")
# max(list5)
# TypeError: '>' not supported between instances of 'str' and 'int'


