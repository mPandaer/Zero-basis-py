# coding=utf-8

"""
    字典类型
        表示的一种映射关系，key与value之间得映射关系
"""

print("==定义字典的两种方式==")
dict1 = {1: 2, 2: 3}
dict2 = dict({1: 2, 2: 3})
print(dict1, id(dict1), type(dict1))
print(dict2, id(dict2), type(dict2))
print("id(dict1) == id(dict2)", id(dict1) == id(dict2))
print()
print("==字典中key和value能定义的类型==")
dict1 = {1: 2, 3: 4}
dict2 = {1: "111", 2: "222"}
dict3 = {1: True, 0: False}
dict4 = {1: None, 2: None}
dict5 = {1: [1, 2], 2: [3, 4]}
dict6 = {1: (1, 2), 2: (3, 4)}
dict7 = {1: {1: 1}, 2: {2: 2}}
print(dict1)
print(dict2)
print(dict3)
print(dict4)
print(dict5)
print(dict6)
print(dict7)
print()
dict1 = {"1a": 2, 3: 4}
dict2 = {"1a": "111", 2: "222"}
dict3 = {"1a": True, 0: False}
dict4 = {"1a": None, 2: None}
dict5 = {"1a": [1, 2], 2: [3, 4]}
dict6 = {"1a": (1, 2), 2: (3, 4)}
dict7 = {"1a": {1: 1}, 2: {2: 2}}
print(dict1)
print(dict2)
print(dict3)
print(dict4)
print(dict5)
print(dict6)
print(dict7)
print()

dict1 = {True: 2, False: 4}
dict2 = {True: "111", False: "222"}
dict3 = {True: True, False: False}
dict4 = {True: None, False: None}
dict5 = {True: [1, 2], False: [3, 4]}
dict6 = {True: (1, 2), False: (3, 4)}
dict7 = {True: {1: 1}, False: {2: 2}}
print(dict1)
print(dict2)
print(dict3)
print(dict4)
print(dict5)
print(dict6)
print(dict7)
print()

dict1 = {(1, 2): 2, (1, 2): 4}
print(dict1)

# TypeError: unhashable type: 'list'
# dict5 = {[1,2]: [1, 2], [3,4]: [3, 4]}
# print(dict5)

# TypeError: unhashable type: 'dict'
# dict2 = {{1: 1}: {1: 1}, {2: 2}: {2: 2}}
# print(dict2)

print()
print("==成员运算符(key)==")
dict1 = {1: 0, 3: 4}
res1 = 3 in dict1
print(res1)
print()
print("==max&min函数(key)==")
res1 = max(dict1)
res2 = min(dict1)
print(res1)
print(res2)

