if 1 < 2 :
    print("yes")

((a,b),c) = ('SP','AM')
print(a+' '+b+' '+c)
print(a,b,c)

L  = [1,2,3,4]
while L:
    front,L = L[0],L[1:]
    print(front,L)

seq = [1,2,3,4]
a,*b = seq
print(a,b)

*a,b = seq
print(a,b)

a,*b,c = seq
print (a,b,c)

for a,*b,c in [(1,2,3,4),(5,6,7,8)]:
    print(a,b,c)