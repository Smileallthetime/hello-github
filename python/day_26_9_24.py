# L = []
# n = 1
# while n <= 99:
#     L.append(n)
#     n = n + 2
#
# print(L)

# L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
#
# r = []
# n = 3
# for i in range(n):
#     r.append(L[i])
#
# print(r)

# print(L[0:4])
# print(L[-3:-1])

# L = list(range(100))
# print(L[:10])
# print(L[-10:])
# print(L[10:20])
# print(L[:10:2])
# print(L[::5])
# print(L[:])

# print((0,1,2,3,4,5,6,7,8,9)[::2])

# print('ABCDEFGHIJKLMNOPQRSTUVWXYZ'[::2])

# def trim(s):
#     if not isinstance(s,str):
#         raise TypeError('not str')
#     while s and s[0] == ' ':
#         s = s [1:]
#     while s and s[-1] == ' ':
#         s = s [:-1]
#     return s
#
# 测试:
# if trim('hello  ') != 'hello':
#     print('测试失败!')
# elif trim('  hello') != 'hello':
#     print('测试失败!')
# elif trim('  hello  ') != 'hello':
#     print('测试失败!')
# elif trim('  hello  world  ') != 'hello  world':
#     print('测试失败!')
# elif trim('') != '':
#     print('测试失败!')
# elif trim('    ') != '':
#     print('测试失败!')
# else:
#     print('测试成功!')

# def findMinAndMax(L):
#     if not isinstance(L, list):
#         raise TypeError('not list')
#     if L == []:
#         return (None, None)
#     else:
#         for i in L:
#             a = max(L)
#             b = min(L)
#             return (b, a)
#
# if findMinAndMax([]) != (None, None):
#     print('1测试失败!')
# elif findMinAndMax([7]) != (7, 7):
#     print('2测试失败!')
# elif findMinAndMax([7, 1]) != (1, 7):
#     print('3测试失败!')
# elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
#     print('4测试失败!')
# else:
#     print('测试成功!')

