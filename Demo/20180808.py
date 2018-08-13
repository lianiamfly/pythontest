# f = open("20180803test.py",'r', encoding='UTF-8')
# print(max(f))
# flag = True
# while flag:
#     try:
#         print(f.__next__())
#     except Exception as err:
#         print(err)
#         flag = False
# else:
#     print("循环完成")

#最快速的读取文本的方法
# for line in open("20180803test.py","r",encoding="UTF-8"):
#     print(line,end=' ')

# import os
# P = os.popen('dir')
# P = P.__iter__()
# while True:
#     try:
#         print(P.__next__())
#     except StopIteration:
#         break
# else:
#     print("Over")

# L = [1,2,3,4,5]
# # for i in range(len(L)):
# #     L[i] = L[i] * 5
# # else:
# #     print(L)
# L = [ x ** 2 for x in L]
# print(L)
# #上面的集合解析表达式中， x ** 2 是循环变量 , for x in L 可以看做是for循环的头部，声明了一个循环变量，以及一个可迭代对象 for x in  L
#
# f = open("20180803test.py","r",encoding='UTF-8')
# lines = f.readlines()
# lines = [ x.rstrip() for x in lines]
# print(lines)
# # lines2 = f.readlines()
# lines2 = [ line.rstrip() for line in open("20180803test.py","r",encoding="UTF-8") if line.__contains__("数量")]
# print(lines2)
#
# #循环嵌套，附加if判定
# L = [x + y for x in "abcdefg" if x >= 'c' for y in "123" if int(y) >1]
# print(L)
# X = (1,2)
# Y = (3,4)
# T1 = list(zip(X,Y))
# print(T1)
# A,B = zip(*zip(X,Y))
# print(A)
# print(B)
# import sys
# print(help(sys.getrefcount))
