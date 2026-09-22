# name = input()
# print('hello,',name)

# name = input('please enter your name = ')
# print('hello,',name)

# print('1024 * 768 =',1024*768)

# a = 100
# if a >= 0:
#     print(a)
# else:
#     print(-a)

# print('I\'m \"OK\"!')
# print('I\'m learning\npython!')
# print('\\\n\\')
# print('\\\t\\')
# print(r'\\\n\\')

# print('''line1
# line2
# line3''')

# print('line1'
#       'line2'
#       'line3')

# print(r'''line1\nline2\nline3''')

# print('''line1\nline2\nline3''')

# True
# False
# not True
# not False

# age = input('Please enter your age = ')
# 把字符串转换为整数
# age = int(age)
# if age >= 18:
#     print('adult')
# else:
#     print('teenager')

# n = 123
# f = 456.789
# s1 = 'Hello, world'
# s2 = 'Hello, \'Adam\''
# s3 = r'Hello, "Bart"'
# s4 = r'''Hello,
# Bob!'''

# print(n)
# print(f)
# print(s1)
# print(s2)
# print(s3)
# print(s4)

# print('中文测试正常')

# print('%2d-%02d' % (3,1))
# print('%.2f' % (3.1415926))

# s1 = 72
# s2 = 85
# r = s2 - s1
# print('%.1f%%' % (r))

# L = [
#     ['Apple','Google','Microsoft'],
#     ['Java','Python','Ruby','PHP'],
#     ['Adam','Bart','Bob']
# ]
# print(L[0][0])
# print(L[1][1])
# print(L[2][2])

# a = input('please enter your age = ')
# age = int(a)
# if age >= 18:
#     print('adult')
# elif age >= 6:
#     print('teenager')
# else:
#     print('kid')

# x = 2
# if x:
#     print('True')
# else:
#     print('False')

# h = input('please enter your height(m) = ')
# w = input('please enter your weight(kg) = ')
# height = float(h)
# weight = float(w)
# bmi = weight / height**2
# BMI = round(bmi,2)
# if BMI > 32:
#     print('your BMI =',BMI,'严重肥胖')
# elif BMI >= 28:
#     print('your BMI =',BMI,'肥胖')
# elif BMI >= 25:
#     print('your BMI =',BMI,'过重')
# elif BMI >= 18.5:
#     print('your BMI =',BMI,'正常')
# else:
#     print('your BMI =',BMI,'过轻')

# score = 'B'
#
# match score:
#     case 'A':
#         print('score is A.')
#     case 'B':
#         print('score is B.')
#     case 'C':
#         print('score is C.')
#     case _:
#         print('score is ???.')

# a = input('please enter your age = ')
# age = int(a)
#
# match age:
#     case x if x < 10:
#         print(f'< 10 years old: {x}')
#     case 10:
#         print('10 years old.')
#     case 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18:
#         print('11~18 years old.')
#     case 19:
#         print('19 years old.')
#     case _:
#         print('not sure.')

# args = ['gcc','hello.c','world.c','111','222']
#
# match args:
#     case ['gcc']:
#         print('gcc: missing source file(s).')
#     case ['gcc',file1,*files]:
#         print('gcc compile: ' + file1 + ', ' + ', '.join(files))
#     case ['clean']:
#         print('clean')
#     case _:
#         print('invalid command.')

# L = ['Bart','Lisa','Adam']
# for name in L:
#     print(f'Hello,{name}!')

# sum = 0
# for x in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
#     sum = sum + x
# print(sum)

# sum = 0
# for x in range(101):
#     sum = sum + x
# print(sum)

# sum = 0
# n = 99
# while n > 0:
#     sum = sum + n
#     n = n - 2
# print(sum)

# n = 1
# while n <= 100:
#     print(n)
#     n = n + 1
# print('END')

# n = 1
# while n <= 100:
#     if n > 10:
#         break
#     print(n)
#     n = n + 1
# print('END')

# n = 0
# while n < 10:
#     n = n + 1
#     print(n)

# n = 0
# while n < 10:
#     n = n + 1
#     if n % 2 == 0:
#         continue
#     print(n)
