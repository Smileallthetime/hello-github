# print('hello world')

# n1 = 255
# n2 = 1000
# a = hex(n1)
# b = hex(n2)
# 转换成十六进制表示
# print(a)
# print(b)

# n = input('please enter your number = ')
# x = int(n)
# def f(x):
#     if x >= 0:
#         return x
#     else:
#         return -x
# print(f(x))

# def nop():
#     pass

# if age >= 18:
#     pass

# def f(x):
#     if not isinstance(x,(int,float)):
#         raise TypeError('bad operand type')
#     if x >= 0:
#         return x
#     else:
#         return -x
# print(f('1'))

# import math
#
# def move(x,y,step,angle=0):
#     nx = x + step * math.cos(angle)
#     ny = y - step * math.sin(angle)
#     return nx, ny

import math

# def quadratic(a,b,c):
#     if b**2 - (4*a*c) < 0:
#         raise ValueError('无实数解')
#     elif a == 0:
#         raise ValueError('a不能等于0')
#     n1 = -b + math.sqrt(b**2 - 4*a*c)
#     n2 = -b - math.sqrt(b**2 - 4*a*c)
#     x1 = n1 / (2*a)
#     x2 = n2 / (2*a)
#     return x1, x2
#
# print('quadratic(2, 3, 1) =', quadratic(2, 3, 1))
# print('quadratic(1, 3, -4) =', quadratic(1, 3, -4))
#
# if quadratic(2, 3, 1) != (-0.5, -1.0):
#     print('测试失败')
# elif quadratic(1, 3, -4) != (1.0, -4.0):
#     print('测试失败')
# else:
#     print('测试成功')

# def mul(x,*args):
#     sum = x
#     for n in args:
#         sum = sum * n
#     return sum
#
# 测试
# print('mul(5) =', mul(5))
# print('mul(5, 6) =', mul(5, 6))
# print('mul(5, 6, 7) =', mul(5, 6, 7))
# print('mul(5, 6, 7, 9) =', mul(5, 6, 7, 9))
# if mul(5) != 5:
#         print('mul(5)测试失败!')
# elif mul(5, 6) != 30:
#         print('mul(5, 6)测试失败!')
# elif mul(5, 6, 7) != 210:
#         print('mul(5, 6, 7)测试失败!')
# elif mul(5, 6, 7, 9) != 1890:
#         print('mul(5, 6, 7, 9)测试失败!')
# else:
#     try:
#         mul()
#         print('mul()测试失败!')
#     except TypeError:
#         print('测试成功!')

# def fact(n):
#     if n==1:
#         return 1
#     return n * fact(n - 1)

# def fact(n):
#     return fact_iter(n,1)
#
# def fact_iter(num,product):
#     if num == 1:
#         return product
#     return fact_iter(num-1,num * product)

# def move(n, a, b, c):
#     if n == 1:
#         print(a,'-->',c)
#     if n > 1:
#         move(n-1, a, c, b)
#         print(a,'-->',c)
#         move(n-1, b, a, c)
#
# move(3, 'A', 'B', 'C')



