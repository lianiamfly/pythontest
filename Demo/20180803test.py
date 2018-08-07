
t = 1 if 1 > 2 else 2
print(t)

x = "spam"
while x :
    print(x,end=' ')
    x = x[1:]
else:
    print("\nover")

a = 0 ; b = 10
while a < b :
    print(a,end=' ')
    a += 1

print("\n")
x = 100 ; y = 0
while x :
    x = x - 1
    if x % 2 != 0 : continue
    print(x,end=' ')
    y += 1
print("数量：",y,end=' \n')

# while True:
#     name = input("请输入名称:")
#     if name == 'stop':
#         print("结束break\n")
#         break
#     age  = input("请输入年龄:")
#     print("Hello!",name,"=>",int(age)**2)
# else:
#     print("结束\n")
#
# x = "test"
# while x:
#     if match(x[0]):
#         print("Ni")
#         break
#     x = x[1:]
# else:
#     print("not found")
sum = 0;
mul = 1;
x = [1,4,3,5,6,8,11]
for cur in x:
    sum += cur
    mul *= cur
else:
    print("待处理列表数据:",x)
    print("和为:",sum)
    print("积为:",mul)

T = [(1,2),(3,4),(5,6)]
for (a,b) in T:
    print(a,b)

D = {'a':1,'b':2,'c':3}
for (key,value) in D.items():
    print("key:",key,"=> value:",value)

D = [(1,2,3,4),(5,6,7,8)]
for (a,*b,c) in D:
    print(a,b,c,sep=' ')

items = ["sd","12",1,2,3,(2,3),1.11]
test = ["sd",1.12]
for key in test:
    for t in items:
        if t == key:
            print(key," was found")
            break
    else:
        print(key," was not found")

print(list(range(0,10,2)))
print(list(range(2,4)))
print(list(range(-10,5,2)))

x = "spam"
print(list(range(len(x))))
for  i in range(len(x)):
    print(i,' ',x[i],end=' ')

print("\n")
x = "abcdefghijklmnopqrst"
for c in x[::2]:
    print(c,end=' ')
#http://idea.iteblog.com/key.php

x = [1,2,3,4]
y = [5,6,7,8]
z = [9,10,11,12]
print("\n")
for (m,n) in list(zip(x,y)):
    print("m: ",m," n: ",n)
else:
    print(list(zip(x,y)))
    print(list(zip(x,y,z)))
