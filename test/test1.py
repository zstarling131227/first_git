###调节
while 1:
    while 1:
        break######后执行的语句为print(2)，而不是返回执行物理行第二行while 1
        print(1)
    print(2)
    break######后执行的语句为print(3)，而不是返回执行物理行第二行while 1
print(3)
"""
输出结果为
2
3
"""
# while 1:
#     while 1:
#         break######后执行的语句为物理行第18行break
#         print(1)
#     break######后执行的语句为print(3)，而不是返回执行物理行第二行while 1
#     print(2)
# print(3)
"""
输出结果为
3
"""

# while 1:
#     while 1:
#         break###后执行的语句为print(2)
#         print(1)
#     print(2)#####后执行的语句为物理行第27行while 1:此时进入无限的循坏
# print(3)

"""
输出结果为
2
2
2
……无数个
2
2
2
2
3
"""

# list1=[1,[1,2,['达内']],3,5,8,13,18]
# list1[1][2][0]='达内教育'###法1
# list1[1][2]=['达内教育']###法2
# print(list1)

"""
红黄蓝 336
摸出8个球
"""
# i=0
# j=0
# for i in range(4):
#     for j in range(4):
#         z=8-(i+j)
#         if z<7:
#             print(i,j,z)
#         j+=1
#     i+=1
#     j=0

"""
水仙花100~999之间
153=1^3+5^3+3^3
"""
# sum_num=0
# for i in range(100,1000):
#     baiweishu=i//100
#     shiweishu =i%100//10
#     geweishu =i%10
#     if i==baiweishu**3+shiweishu**3+geweishu**3:
#         print(i)
#         sum_num+=i
# print(sum_num)