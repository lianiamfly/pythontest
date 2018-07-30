# x = 'spam'
# y = 99
# z = ['eggs']
# print(x, y, z)
# print(x, y, z, sep=';')
# print(x, y, z, end='...\n')
#
# print(x, y, z, file=open('temp1', 'w'))
# print(x, y, z, file=open('temp2', 'w'))
# print(x, y, z, file=open('temp3', 'w'))
# print(open('temp1', 'rb').read(), open('temp2', 'rb').read(), open('temp3', 'rb').read())
#
# x = 1
# if x:
#     y = [1,
#          2,
#          3]
#     z = (1,2,
#          3)
#     if y:
#         print(y,z,sep=' ； ')
#     print("block1")
# print("block0")

import  requests

r = requests.get('https://api.github.com/events')
print(r.json())