# x = [1, 'Two', 3, 'Four']
# y = [1, 'Two', 3, 'Four']
# z = [1]
# print(x[2:3])
# print(x[2:3] == 3)
# print(x is y)
# print(x == y)
# print(z in x)

# a = 21 % 2.5
# print(a)

# a = {'one': 1, 'two': 2, 'three': 3}
# a['one'] += 1
# print(a['one'])

# for num in range(10):
#    if (num % 2 == 1):
#        continue
#    print(num)

# A.每个对象都一定会有__dict__属性(错误)
# 只有类实例才会有__base__属性,当一个类内有__slots__列表时，此类生成的对象没有__dict__属性
# B.每个对象都一定有 __doc__ 属性 
# C.__dict__属性用来绑定实例变量的字典
# D.每个对象都一定有 __class__属性

# class A:
#    v = 100
#    def __init__(self):
#        self.v = 200
# a1 = A()
# a2 = A()
# del a2.v
# print(a1.v)
# print(A.v)
# print(a2.v)
# print(a1.__class__.v)

# print("hello world".split(" "))

# a = [("b",2), ("a",1), ("c", 1),  ("d",4)]
# b = a.sort()
# print(a, b)

# print(set({1: "1", 2: "2", 5: "5"}))

# def fun01():
#     yield 1
# fun01()

# S ="ABCDEFG"
# ##print(S[-2,-5])

# for x in range(5, 0, -2):
#     print(x)

# print(float('-3.14'))
# # int('-3.14')
# print(int(-3.14))
# print(str(-3.14))

# print(list("Hello world"))

# d = {"a": 3, "b": 2, "c": 1}
# print(max(d))

# L1 = [1, 2, 3]
# L2 = [L1, 4, 5]
# L3 = L2
# L4 = L3.copy()
# L1[1] = 10
# L3[1] = 40
# L4[2] = 50
# print(L1)
# print(L2)
# print(L3)
# print(L4)

# print ("%s 今年 %d 岁"  %  ("小明", 20))
# # print("小明"+'今年'+20+'岁')
# # print ("%s 今年 %d 岁"  %  "小明", 20)
# print("小明" '今年', 20, '岁')

# print(5 > 3 == True)
# print(5> 3 < 8)
# print(bool("  "))
# print(bool(None))
# 布尔值只有真（True）和假（False）两种。bool(x)函数可以返回对象x的对应的布尔值，None、空字符串、空列表，空元组、空字典，数值0等的布尔值是False，其他是真。关系表达式 5>3<8 相当于 5>3 and 3 < 8同理，5>3==True 相当于5>3 and  3 == True。布尔值只有真（True）和假（False）两种。bool(x)函数可以返回对象x的对应的布尔值，None、空字符串、空列表，空元组、空字典，数值0等的布尔值是False，其他是真。关系表达式 5>3<8 相当于 5>3 and 3 < 8同理，5>3==True 相当于5>3 and  3 == True。


# class A:
#    def __init__(self):
#        self._a = 100
#        self.__b = 200
#        self.__c_ = 300
#        self.__d__ = 400
# a = A()
# # print(a.__c_)
# print(a.__d__)
# print(a._a)
# # print(a.__b)

# # dict内有__getitem__方法
# print(dir(dict))
# # int类内有__mod__方法
# print(dir(int))
# # set内有__add__方法
# print(dir(set))
# # list类内有__iadd__方法
# print(dir(list))

# print(5 > 3 == True)
# print(5> 3 < 8)
# print(bool("  "))
# bool(None)

# # print("I am" + 20 + "years old")
# print(int(1.5))
# # print(int("99.1"))
# print("abcd" * 6)

# num = 1
# while num <= 20:
#    print(num)
#    num += 1
# else:
#    print("打印完毕")

# a = frozenset((1,2,3))
# b = {2, 3, 4}
# print(a-b)
# # print(a+b)
# print(a in b)
# print(a & b)

# def bar(multiple):
#     def foo(n):
#         return multiple**n
#     return foo
# print(bar(2)(3))

# import math
# print(math.floor(5.5))
# print(type(1/2))

# a=(1,2,3)
# # print(a[1:-1])
# # print(a*3)
# print(a[2]==4)
# # print(list(a))

# a=range(100)
# print(a)
# print(type(a))
# print(a[-3])

