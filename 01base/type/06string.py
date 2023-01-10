# coding:utf-8

"""
    字符串类型
"""

print("==定义字符串的两种方式==")
str1 = "pandaer杂货铺"
str2 = str("pandaer杂货铺")
print('str1 = "pandaer杂货铺" 的类型: ' + str(type(str1)))
print('str2 = str("pandaer杂货铺") 的类型: ' + str(type(str2)))

print("==成员运算符==")
exist = 'pandaer' in str1
print("'pandaer' in str1 :", exist)

print("==max() & min() 函数==")
max_str = max(str1)
min_str = min(str1)
print("最大的字符:", max_str, "最小的字符:", min_str)

print("==字符串的不可变性==")
string1 = "pandaer"
string2 = "pander"
print(string1, id(string1))
print(string2, id(string2))
print("id(string1) == id(string2)?", id(string1) == id(string2))

