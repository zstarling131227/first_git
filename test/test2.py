###2;
# a=1
# def fun(a):
#     a=2
# fun(a)
# print(a)

# a=[]
# def fun01(a):
#     a.append(1)
# fun01(a)
# print(a)


####3;
# list01=[1,2,3,4,5]
# def square(x):  # 计算平方数
#     return x ** 2
# list04=map(square, [1, 2, 3, 4, 5])  # 计算列表各个元素的平方
# print(list(list04))
# list05=list(map(lambda x: x ** 2, [1, 2, 3, 4, 5]))  # 使用 lambda 匿名函数
# print(list05)
# # 提供了两个列表，对相同位置的列表数据进行相加
# list06=list(map(lambda x, y: x + y, [1, 3, 5, 7, 9], [2, 4, 6, 8, 10]))
# print(list06)
#
# listx = [1,2,3,4,5,6,7]       # 7 个元素
# listy = [2,3,4,5,6,7]         # 6 个元素
# listz = [100,100,100,100]     # 4 个元素
# list_result = map(lambda x,y,z : x**2 + y + z,listx, listy, listz)
# print(list(list_result))

# list03=map(square,list01)
# list02=list(list03)
# print(list02)
# list10=[]
# for i in list02:
#     if i>10:
#         list10.append(i)
# print(list10)

# list1=[i for i in list02 if i>10]
# print(list1)

# list1=[i for i in list(map(square,list01)) if i>10]
# print(list1)

"""
for i in list02:
    print(i)
    if i>10:
        list02.append(i)##写法错误，list02一直添加元素，for 循环移至在进行，从而会进入无限循坏
print(list02)
"""
###6;
seq=[{"name": "Mcoy", "age":18},
     {"name":"Adam","age":28},
     {"name":"Talor","age":26},
     {"name":"Charlie","age":15}]
# max_age=listb[0]["age"]
# print(min_age)
# list01=[]
# for i in range(len(listb)):
#     print(i)
#     print(listb[i]["age"])
#     if listb[i]["age"]>max_age:
#         max_age=listb[i]["age"]
#         list01.append(listb[i])

for i in range(len(seq)):
    for j in range(i, len(seq)):
        if seq[j]["age"]>seq[i]["age"]:
            seq[i]["age"], seq[j]["age"]= seq[j]["age"], seq[i]["age"]
# print(listb)

######7;(画内存图)
import copy
a=[1,2,3,4,['a','b']]
b=a
c=copy.copy(a)
d=copy.deepcopy(a)
a.append(5)
a[4].append("c")
# print(a)
# print(b)
# print(c)
# print(d)

######８；
A0=dict(zip(('a','b','c','d','e'),(1,2,3,4,5)))
# A1=range(10)
# A2=[i for i in A1 if i in A0]
# A3=[]
# for s in A0:
#     print(s)####此时取出的是字典Ａ０的键值
#     # print(A0[s])
#     # A3.append(A0[s])
# print(A3)
#
# for s,value in A0.items():
#     print(s)
#     print(value)
# A3=[A0[s] for s in A0]###有难度

# A4=[i for i in A1 if i in A3]
# A5={i:i*i for i in A1}
# A6=[[i,i*i] for i in A1]

# print(A0)
# print(A1)
# print(A2)
# print(A3)
# print(A4)
# print(A5)
# print(A6)



####17;
seq=[5,6,78,12,9,0,-1,2,3,-65,12]
for i in range(len(seq)):
    for j in range(i, len(seq)):
        if seq[j]>seq[i]:
            seq[i] ,seq[j]= seq[j], seq[i]
print(seq)

