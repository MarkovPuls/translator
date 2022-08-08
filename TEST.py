"""Файл для задач на stepik"""

# a, b, c = map(int, input().split())
# print(a + b + c * 2)

# a + a + (a + a) * 2 = c

# c = int(input())
# a = int(c / 6)
# b = a * 4
# d = a
# print(a, b, d)

# a, b, c = map(int, input().split())
# q = a * 3
# w = b * 5
# e = c * 12
# print(q + w + e)


# a, b, c = map(int, input().split())
# m = a * b * c * 2
# print(m)

# a, b, c, d = map(int, input().split())
# m = (a + b + c + d) / 4
# print(m)

# a1 = int(input())
# a2 = int(input())
# a3 = int(input())
# b1 = int(input())
# b2 = int(input())
# b3 = int(input())
#
# ac1 = a1 * 3600
# ac2 = a2 * 60
# ac3 = ac1 + ac2 + a3
#
# bc1 = b1 * 3600
# bc2 = b2 * 60
# bc3 = bc1 + bc2 + b3
#
# print(bc3 - ac3)

# a = int(input())
# b = int(input())
# c = abs(a) + abs(b)
# print(c)

# a, b, c, d, e = map(int, input().split())
# m = max(a, b, c, d, e)
# print(m)

# a = float(input())
# b = round(a, 2)
# c = round(a, 3)
# print(b, c)


# print(1, 2, 3, sep='RRRR', end='!!!')
# a = 10
# b = 20
# print('Я пишу текст %s и вставляю %s переменные'% (a, b))

# a, b, c = map(int, input().split())
# print(a, b, c, sep=',')

# a = int(input())
# b = a - 1
# c = a + 1
# print(b, a, c, sep='<')

# a = input()
# b = input()
# c = input()
# print(a, b, c, sep='---')

# a = input()
# print(1, 2, 3, 4, 5, sep=a)

# a = int(input())
# b = a // 1000
# print(b)

# n = int(input())
# k = int(input())
# a = n // k
# print(a)

# n = int(input())
# print(n % 1000 // 100)

# n = int(input())
# a = n % 10 // 1
# b = n % 100 // 10
# c = n % 1000 // 100
# print(a + b + c)

# n = int(input())
#
# a = n // 100
# a1 = n - (a * 100)
#
# b = a1 // 20
# b1 = n - a * 100 - b * 20
#
# c = b1 // 10
# c1 = n - a * 100 - b * 20 - c * 10
#
# d = c1 // 5
# d1 = n - a * 100 - b * 20 - c * 10 - d * 5
#
# e = d1 // 1
#
# print(a + b + c + d + e)

# n = int(input())
# m = n % 1440
# a = m // 60
# b = m % 60
# print(a, b)

# n = int(input())
# m = n % 2
# a = n + 2 - m
# print(a)

# n = int(input())
# a = n % 60
# b = (n // 60) % 60
# c = ((n // 60) // 60) % 60
# a1 = str(a).zfill(2)
# b1 = str(b).zfill(2)
# c1 = c // 10, c % 10
# print(c, str(b1), a1, sep=':')

# n = int(input())
# m = n % 10 == 2
# print(m)

# a, b = map(int, input().split())
# m = a % 7 == 0 and b % 7 == 0
# print(m)

# a, b, c = map(int, input().split())
# m = a == b and b == c
# print(m)

# n = int(input())
# m = 5 < n <= 19
# print(m)

# a = str(input())
# b = str(input())
# m = a == 'awesome' or b == 'awesome'
# print(m)

# a, b, c = map(int, input().split())
# m = a == b or a == c
# print(m)

# n = int(input())
# m = 9 < n < 100
# print(m)

# a, b, c = map(int, input().split())
# m = a ** 2 + b ** 2 == c ** 2 or a ** 2 + c ** 2 == b ** 2 or b ** 2 + c ** 2 == a ** 2
# print(m)

# import math

# a = int(input())
# b = int(input())
# c = int(input())
# a1 = math.ceil(a/2)
# b1 = math.ceil(b/2)
# c1 = math.ceil(c/2)
# m = a1 + b1 + c1
# print(m)

# a, b, c = map(int, input().split())
# m = (a * c) * 2 + (b * c) * 2
# d = math.ceil(m/16)
# print(d)

# m = 'Лев Николаевич Толстой написал "Война и мир"'
# print(m)

# a = str(input())
# b = str(input())
# # c = a + '\n'
# print(a)
# print(b)
#
# a = input()
# b = input()
# c = input()
# print(c)
# print(b)
# print(a)

# a = str(input())
# print(a + ' ' + a + ' ' + a + ' ' + a)

# a = str(input())
# print(len(a))

# a = str(input())
# print(a * 3)

# a, b, c = map(str, input().split())
# a1 = ord(a)
# b1 = ord(b)
# c1 = ord(c)
# print('Simvol code', a, 'is', a1, end='.\n')
# print('Simvol code', b, 'is', b1, end='.\n')
# print('Simvol code', c, 'is', c1, end='.\n')

# m = input()
# print(m[::2])

# m = input()
# print(m[::-1])

# m = input()
# n = m[-1]
# print(n + m[:-1])

# m = input().upper()
# print(m)

# a = input().lower()
# b = a.count('e')
# print(b)

# a = input()
# b = a.replace('w', '')
# print(b.replace('z', ''))

# a = input().rfind('a')
# print(a)

# a = len(input().split())
# print(a)

# a = input().replace(' ', ',')
# print(a)

# print('/\_/\ \n>^,^<\n / \ \n(|_|)_/')

# print(r'  /~~~\  ')
# print(r' //^ ^\\ ')
# print(r'(/(_*_)\)')
# print(r"_/''*''\_")
# print(r'(/_)^(_\)')

# a = input()
# b = input()
# print('Здравствуйте, {a} {b}!'.format(a=a, b=b))

# a = int(input())
# b = a - 1
# c = a + 1
# print('Для числа {a} предыдущим будет число {b}.\nДля числа {a} следующим будет число {c}.'.format(a=a, b=b, c=c))

# a = input()
# b = int(input())
# print(f'{a}, вам исполнится 77 лет в {b + 77}')

# a = int(input())
# print(f'{a} сек - это {a // 60} мин. {a % 60} сек.')

# a, b = map(int, input().split())
# print(f'Разрешение экрана: {a} x {b}.\nОбщее количество пикселей = {a * b}.')

# a = int(input())
# b = int(input())
#
# print(f'{a} / {b} = {a/b}\n{a} // {b} = {a//b}\n{a} % {b} = {a%b}')

# a = int(input())
# b = int(input())
# c = int(input())
# print(f'Vector A({a}, {b}, {c})\nVector B({a + 5}, {b + 5}, {c + 5})')

# a = float(input())
# b = int(input())
# print(f'Current dollar rate is {a}. You want buy {b} dollars\nYou must pay {a * b}')

# my_list = list(map(int, input().split()))
# print(777 in my_list)

# a = list(map(int, input().split()))
# print(min(a), max(a))

# a = list(map(int, input().split()))
# print(sum(a)/len(a))

# a = list(map(int, input().split()))
# print(a[::-1])

# top = ['Игра престолов', 'Шерлок', 'Друзья', 'Во все тяжкие', 'Доктор Хаус', 'Теория большого взрыва', 'Бригада']
# top[-1] = "Сверхъестественное"
# top[2] = "Настоящий детектив"
# print(top)

# a = list(map(int, input().split()))
# print(a.count(999))

# a = list(map(str, input().split()))
# b = '-'.join(a[0]).upper()
# c = '-'.join(a[1]).upper()
# print(b, c)

# a = list(map(str, input().split()))
# b = '\n'.join(a)
# print()

# a = list(map(str, input().split()))
# b = '.'.join(a[0])
# c = '.'.join(a[1])
# print(a[2], b[0:2] + c[0:2])

# a = int(input())
# if a >= 20000:
#     print(a - a / 100 * 13)
# else:
#     print(a)

# a = str(input())
# if a == 'Python':
#     print('ДА')
# else:
#     print('НЕТ')

# a = int(input())
# b = int(input())
# if a > b:
#     print(a)
# else:
#     print(b)

# a = str(input())
# b = ''.join(a)
# if a == b[::-1]:
#     print('YES')
# else:
#     print('NO')

# a, b, c = map(int, input().split())
# if a + b == c:
#     print('YES')
# else:
#     print('NO')

# a = str(input())
# b = str(input())
# c = ''.join(a)
# if b == c[::-1]:
#     print('YES')
# else:
#     print('NO')

# a = int(input())
# b = int(input())
# c = int(input())
# if a + b > c and a + c > b and b + c > a:
#     print('YES')
# else:
#     print('NO')


# a = list(map(int, input()))
# b = int(len(a) / 2)
# c = a[:b]
# d = a[b:]
# if sum(c) == sum(d):
#     print('YES')
# else:
#     print('NO')
# print(c, d)

# a = list(map(int, input()))
# b = a[-3:]
# c = a[:-3]
# if sum(b) == sum(c):
#     print('YES')
# else:
#     print('NO')
# print(b, c)

# a = int(input())
# if a % 2 == 0:
#     print(a // 2)
# else:
#     print(a // 2 - a)

# s = ' abcdefgh'
# a1 = input()
# a2 = input()
# b1 = a1[0]
# b2 = a2[0]
# c1 = s.find(b1)
# c2 = s.find(b2)
# d1 = int(a1[1])
# d2 = int(a2[1])
# if (d1 + c1) % 2 == 0 and (d2 + c2) % 2 == 0 or (d1 + c1) % 2 == 1 and (d2 + c2) % 2 == 1:
#     print('YES')
# else:
#     print('NO')

# a = int(input())
# b = int(input())
# if a < b:
#     print("<")
# else:
#     if a > b:
#         print('>')
#     else:
#         print("=")

# a = int(input())
# b = int(input())
# c = int(input())
# if a > b:
#     if a > c:
#         print(a)
#     else:
#         print(c)
# else:
#     if b > c:
#         print(b)
#     else:
#         print(c)

# a = int(input())
# if a == 1:
#     print(0)
# else:
#     if a % 2 == 0:
#         print(int(a/2))
#     else:
#         print(a)

# a, b, c = map(int, input().split())
# m = int()
# q = int()
# if a > b:
#     if a > c:
#         m = a
#     else:
#         m = c
# else:
#     if b > c:
#         m = b
#     else:
#         m = c
# if a < b:
#     if a < c:
#         q = a
#     else:
#         q = c
# else:
#     if b < c:
#         q = b
#     else:
#         q = c
# print(m - q)

# a = str(input().lower())
# b = str(input().lower())
# if a < b:
#     print(-1)
# if a > b:
#     print(1)
# if a == b:
#     print(0)

# a = int(input())
# if a % 3 == 0 and a % 5 == 0:
#     print("FizzBuzz")
# elif a % 5 == 0:
#     print('Buzz')
# elif a % 3 == 0:
#     print('Fizz')
# else:
#     print(a)

# a = int(input())
# b = int(input())
# c = int(input())
#
# if a == b and a == c:
#     print('3')
# elif a == b or a == c or c == b:
#     print('2')
# else:
#     print('0')

# a = int(input())
# if a == 1:
#     print('Январь')
# elif a == 2:
#     print('Февраль')
# elif a == 3:
#     print('Март')
# elif a == 4:
#     print('Апрель')
# elif a == 5:
#     print('Май')
# elif a == 6:
#     print('Июнь')
# elif a == 7:
#     print('Июль')
# elif a == 8:
#     print('Август')
# elif a == 9:
#     print('Сентябрь')
# elif a == 10:
#     print('Октябрь')
# elif a == 11:
#     print('Ноябрь')
# elif a == 12:
#     print('Декабрь')


# a = int(input())
# if a < 2:
#     print("Младенец")
# elif a < 4:
#     print("Малыш")
# elif a < 12:
#     print("Ребенок")
# elif a < 19:
#     print("Подросток")
# elif a < 65:
#     print("Взрослый человек")
# else:
#     print("Пожилой человек")

# a = float(input())
# b = float(input())
# c = input()
#
# if c == '+':
#     print(a + b)
# elif c == '-':
#     print(a - b)
# elif c == '*':
#     print(a * b)
# elif c == '/':
#     if a == 0 or b == 0:
#         print('Неизвестно')
#     else:
#         print(a / b)
# else:
#     print('Неизвестно')

# a = str(input())
# b = str(input())
# if len(a) < 7:
#     print("Short")
# elif a != b:
#     print("Difference")
# else:
#     print('OK')

# k = 10
# z = 0
# while k <= 14:
#     z = z + k
#     k += 1
# print(z)

# a = 1000
# while a < 2000:
#     print(a)
#     a += 1
# print(a)

# a = 6785
# while a > 195:
#     print(a)
#     a -= 5
# print(a)

# a, b = map(int, input().split())
# m = int()
# while a <= b:
#     a *= 3
#     b *= 2
#     m += 1
# print(m)

# numbers = [2, 3, 7, 9, 5, 0, 6, 3, 6, 0, 1, 7, 9, 4, 4, 4, 2, 2, 6, 9, 1, 7, 0, 3, 8, 1, 0,
#            3, 8, 0, 8, 4, 0, 2, 3, 6, 6, 1, 5, 8, 7, 2, 3, 8, 7, 7, 1, 2, 2, 8, 4, 3, 4, 8,
#            0, 7, 9, 8, 3, 7, 7, 7, 7, 5, 1, 7, 4, 5, 0, 8, 0, 9, 2, 4, 7, 6, 6, 5, 9, 7, 1,
#            7, 8, 8, 3, 4, 9, 7, 6, 4, 2, 0, 0, 0, 9, 4, 0, 9, 4, 4, 4, 5, 5, 4, 2, 5, 9, 4,
#            8, 1, 5, 7, 1, 0, 2, 6, 8, 7, 2, 7, 9, 3, 6, 4, 7, 5, 0, 7, 2, 0, 8, 2, 9, 8, 6,
#            4, 4, 7, 5, 5, 9, 4, 9, 5, 6, 9, 1, 1, 3, 1, 5, 2, 1, 7, 0, 0, 7, 8, 1, 3, 0, 0,
#            4, 4, 3, 3, 6, 7, 8, 6, 1, 2, 0, 2, 0, 9, 9, 0, 5, 2, 4, 1, 7, 4, 9, 9, 4, 9, 6,
#            9, 2, 7, 1, 2, 4, 5, 4, 0, 9, 0]
#
# while numbers.count(4) != 0:
#     numbers.remove(4)
# print(numbers)

# w = input()
# print(w)
# while len(w) > 0:
#     w = w[1:-1]
#     print(w)
# print('end')

# a = int(input())
# m = 1
# while m * m <= a:
#     print(m * m)
#     m += 1

# a, b = map(int, input().split())
# n = 1
# while a <= b:
#     a = a + a * 0.15
#     n += 1
# print(n)

# a, b = map(int, input().split())
# print((a-1)//(b-1)+a)

# m = int(input())
# a = 0
# while 2 ** a < m:
#     a += 1
# if 2 ** a == m:
#     print(a)
# else:
#     print('НЕТ')

# m = int(input())
# a = int(str(m)[0])
# while a != 1 and m <= 10**9:
#     m = m * a
#     a = int(str(m)[0])
# print(m)

# number = 1234567890
# count = 0
# while number > 0:
#     last_digit = number % 10
#     if last_digit < 3:
#         count = count + 1
#     number = number // 10
# print(count)

# number = 73408
# m = 0
# s = 0
# while number > 0:
#     last_digit = number % 10
#     s = s + last_digit
#     if last_digit > m:
#         m = last_digit
#     number = number // 10
# print(s + m)

# a = int(input())
# maxi = 0
# mini = 9
# while a > 0:
#     b = a % 10
#     if b > maxi:
#         maxi = b
#     if b < mini:
#         mini = b
#     a = a // 10
# print(mini)
# print(maxi)

# a = int(input())
# n = 0
# while a > 0:
#     b = a % 10
#     if b == 7:
#         n += 1
#     a = a // 10
# print(n)

# a = int(input())
# while a > 0:
#     m = a % 2
#     print(m)
#     a = a // 2

# a = int(input())
# i = 1
# b = []
# while i <= a:
#     if a % i == 0:
#         b.append(i)
#     i += 1
# if len(b) < 2 and b[0] != 1:
#     print('Yes')
# else:
#     print('No')

# a = int(input())
# i = 1
# b = []
# while i <= a:
#     if a % i == 0:
#         b.append(i)
#     i += 1
# print(sum(b))

# a, b = map(int, input().split())
# q, w = a, b
# while b > 0:
#     c = a % b
#     a = b
#     b = c
# print(int(q * w / a))

# t = 7
# while t > 1:
#     t -= 1
#     if t == 3:
#         break
#     print(t)

# print(list(range(-11, -36, -1)))

# print(list(range(10, -1, -1)))

# print(list(range(1000, 499, -50)))

# for i in range(1, 14):
#     print('Надо было брать биткоин в 2012!')

# a = int(input())
# b = int(input())
#
# for i in range(a, b + 1):
#     if i % 3 == 0 and i % 5 == 0:
#         print('FizzBuzz')
#     elif i % 5 == 0:
#         print('Buzz')
#     elif i % 3 == 0:
#         print('Fizz')
#     else:
#         print(i)

# a = int(input())
# b = int(input())
# for i in range(a, b + 1):
#     print(f'Число {i}; его квадрат = {i**2}; его куб = {i**3}')

# n = int(input())
# m = 0
# k = 0
# for i in range(n):
#     a, b = map(int, input().split())
#     if a > b:
#         m += 1
#     elif a < b:
#         k += 1
# if m > k:
#     print('Mishka')
# elif k > m:
#     print('Chris')
# elif m == k:
#     print('Friendship is magic!^^')

# n = int(input())
# for i in range(n):
#     a = input().lower()
#     if 'рок' in a:
#         print(i + 1, a.find('рок') + 1)

# n = int(input())
# d = []
# for i in range(n):
#     a = input()
#     if 'соль' not in a:
#         d.append(a)
# print(', '.join(d))

# n = int(input())
# d = []
#
# for i in range(n):
#     a = i
#     if i % 3 == 0:
#         d.append(a)
#     elif i % 5 == 0:
#         d.append(a)
# print(sum(d))

# d = []
# for i in range(50, 101):
#     d.append(i**3)
# print(sum(d))

# n = int(input())
# d = []
# for i in range(n):
#     a = input()
#     if len(a) > 10:
#         b = (a[0], str(len(a) - 2), a[-1])
#         c = (''.join(b))
#         d.append(c)
#     else:
#         d.append(a)
# print('\n'.join(d))

# n = int(input())
# a = []
# for i in range(n):
#     d = input()
#     a.append(d)
# print(a)

# a = input()
# b = (input().split())
# q = len(b)
# for i in range(q):
#     if a in b[i]:
#         print(b[i])

# a = input().split()
# d = []
# c = len(a)
# for i in a:
#     if i > '0':
#         d.append(i)
# if len(d) > 0:
#     print(min(d, key = lambda i: int(i)))
# else:
#     print('Empty')

# a = input().lower()
# s = []
# for i in a:
#     s.append(a.count(i))
# print(max(s))

# a = int(input())
# if a % 11 == 0:
#     print('YES')
# else:
#     print('NO')

# a = str(input())
# b = []
# for i in a:
#     if i >= '0' and i <= '9':
#         b.append(i)
# c = map(int, b)
# print(len(b), sum(c))

# a = input()
# s = []
# g = True
# for i in a:
#     if i in '({[':
#         s.append(i)
#     elif i in ')}]':
#         if not s:
#             g = False
#             break
#         o = s.pop()
#         if o == '(' and i == ')':
#             continue
#         if o == '{' and i == '}':
#             continue
#         if o == '[' and i == ']':
#             continue
#         f = False
#         break
# if g and len(s) == 0:
#     print('YES')
# else:
#     print('NO')

# a = input()
# c = [0] * 10
# for i in str(a):
#     b = int(i)
#     c[b] += 1
# for i in range(10):
#     if c[i] > 0:
#         print(i, c[i])

# for n1 in range(4):
#     for n2 in range(4):
#         for n3 in range(4):
#             for n4 in range(4):
#                 print(n1+n2+n3+n4, end='')
#             print()

# m = 0
# for n1 in range(1000, 10000):
#     l1 = str(n1)
#     if int(l1[0]) + int(l1[1]) + int(l1[2]) + int(l1[3]) == 20:
#         m += n1
# print(m)

# a = int(input())
# for i in range(1, a+1):
#     for y in range(1, i+1):
#         print(y, end=' ')
#     print()

# def plain(p):
#     if p % 2 == 0 and p != 2 or p == 1:
#         return False
#     d = 3
#     while d * d <= p:
#         if p % d == 0:
#             return False
#         d += 2
#     return True
#
#
# n = int(input())
# count = 0
# for p in range(n + 1, 2 * n):
#     if plain(p):
#         count += 1
# print(count)

# n, m = map(int, input().split())
# count = 0
# a = 0
# while a ** 2 <= n:
#     b = n - a ** 2
#     if b >= 0 and a + b ** 2 == m:
#         count += 1
#     a += 1
# print(count)

# a = map(int, input().split())
# for i in a:
#     print('*' * i)

# n = int(input())
# m = list(map(int, input().split()))
# count = 0
# for run in range(n - 1):
#     for i in range(n - 1 - run):
#         if m[i] > m[i + 1]:
#             count += 1
#             m[i], m[i + 1] = m[i + 1], m[i]
# print(*m)
# print(count)

# n = int(input())
# m = list(map(int, input().split()))
# for run in range(n - 1):
#     for i in range(n - 1 - run):
#         if m[i] > m[i + 1]:
#             m[i], m[i + 1] = m[i + 1], m[i]
# print(*m)

# q = []
# a = int(input())
# for i in range(a):
#     q.append([0] * a)
# for i in range(a):
#     for j in range(a):
#         if i == j:
#             q[i][j] = 10
#         elif i > j:
#             q[i][j] = 3
#         else:
#             q[i][j] = 5
# for i in q:
#     print(i)

# n = []
# a = int(input())
# for i in range(a):
#     n = i + 1
#     for j in range(a):
#         n = j + 1
#         print(n, end=' ')
#     print()

# a = []
# n = int(input())
# for i in range(n):
#     a.append(list(input().split(' ')))
# m = 0
# for i in range(n):
#     for j in range(n):
#         if i == j:
#             m += int(a[i][j])
# print(m)

# a = []
# n = int(input())
# for i in range(n):
#     a.append(list(input().split(' ')))
# for i in range(n):
#     for j in range(n):
#         print(a[i][j], end=' ')
#     print()

# a = []
# n = int(input())
# for i in range(n):
#     a.append(list(map(int, input().split())))
# for i in range(n - 1, -1, -1):
#     for j in range(n - 1, -1, -1):
#         print(a[j][i], end=' ')
#     print()

# a = []
# n, m = map(int, input().split())
# for i in range(n):
#     a.append(list(map(int, input().split())))
# for i in range(n-1, -1, -1):
#     for j in range(m):
#         print(a[i][j], end=' ')
#     print()

# a = []
# for i in range(5):
#     a.append(list(map(int, input().split())))
# for i in range(5):
#     for j in range(5):
#         if a[i][j] == 1:
#             b = i
#             c = j
# print(abs(2 - b) + abs(2 - c))

# a = []
# n, m = map(int, input().split())
# for i in range(n):
#     a.append(list(map(int, input().split())))
# for j in range(n):
#     q = 0
#     for i in range(m):
#         q += a[j][i]
#     print(q, end=' ')
# print()
# for j in range(m):
#     p = 0
#     for i in range(n):
#         p += a[i][j]
#     print(p, end=' ')

# a = []
# n = int(input())
# for i in range(n):
#     a.append(list(map(int, input().split())))
# c = 0
# d = 0
# for i in range(n):
#     for j in range(n):
#         if i > j:
#             c += a[i][j]
#         elif i < j:
#             d += a[i][j]
# if c == d:
#     print('Yes')
# else:
#     print('No')

# n = int(input())
# zeroes = [1 + i for i in range(n)]
# print(zeroes)

# n = int(input())
# a = [n // (i + 1) for i in range(n) if n % (i + 1) == 0]
# print(sorted(a))

# n = int(input())
# a = [i - 1 for i in range(n * n + 2) if (i + 1) % 2 != 0 and i > n]
# print(a)
from typing import List, Any

# a, b = list(map(int, input().split()))
# if a <= b:
#     n = [i * i for i in range(a, b + 1)]
# elif a > b:
#     n = [i * i * i for i in range(a, b - 1, - 1)]
# print(n)

# from string import ascii_uppercase
# a = ascii_uppercase
# n = int(input())
# m = [i for i in a]
# print(m[:n])

# vector = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]]
# new_list = []
# for i in vector:
#     for j in i:
#         new_list.append(j)
# print(new_list)

# n = int(input())
# b = {}
# a = str([i + 1 for i in range(n)])
# a = a.split()
# m = [i + 1 for i in range(n)]
# for i in a[4:]:
#     b['df'].append(int(i))
# print(b)

# a = {}
# n = int(input())
# for i in range(1, n + 1):
#     a = {i: i ** 2}
# print(a)

# print({x: x**2 for x in range(1, int(input())+1)})

# d1 = {'a': 100, 'b': 200, 'c': 333}
# d2 = {'x': 300, 'y': 200, 'z': 777}
# m = d1
# m.update(d2)
# print(m)

# logs = {}
# n = int(input())
# for i in range(n):
#     log = input()
#     if log in logs:
#         print(f'{log}{logs[log]}')
#         logs[log] += 1
#     else:
#         print('OK')
#         logs[log] = 1

'''6.1'''

# countries = {
#     "Sweden": ["Stockholm", "Göteborg", "Malmö"],
#     "Norway": ["Oslo", "Bergen", "Trondheim"],
#     "England": ["London", "Birmingham", "Manchester"],
#     "Germany": ["Berlin", "Hamburg", "Munich"],
#     "France": ["Paris", "Marseille", "Toulouse"]
# }
#
# city = input()
#
# for key, values in countries.items():
#     if city in values:
#         print(f'INFO: {city} is a city in {key}')
#         exit()
#     else:
#         print(f'ERROR: Country for {city} not found')
#     print(values)

# a = input()
# b = {}
# for i in a.lower():
#     if i.isalpha():
#         b[i] = b.get(i, 0) + 1
# print(b)

# data = {'my_friends': {'count': 10,
#                        'items': [{'first_name': 'Kurt', 'id': 621547005, 'last_name': 'Cobain', 'bdate': '31.8.2005'},
#                                  {'first_name': 'Виолетта', 'id': 484200150, 'last_name': 'Кастилио'},
#                                  {'first_name': 'Иринка', 'id': 21886133, 'last_name': 'Бушуева', 'bdate': '28.8.1942'},
#                                  {'first_name': 'Данил', 'id': 282456573, 'last_name': 'Греков', 'bdate': '4.7.2002'},
#                                  {'first_name': 'Валентин', 'id': 184902932, 'last_name': 'Долматов', 'bdate': '25.5'},
#                                  {'first_name': 'Евгений', 'id': 620469646, 'last_name': 'Шапорин',
#                                   'bdate': '6.12.1982'},
#                                  {'first_name': 'Ангелина', 'id': 622328862, 'last_name': 'Краснова',
#                                   'bdate': '4.11.1995'},
#                                  {'first_name': 'Иван', 'id': 576015198, 'last_name': 'Вирин', 'bdate': '2.2.1915'},
#                                  {'first_name': 'Паша', 'id': 386922406, 'last_name': 'Воронов', 'bdate': '27.9'},
#                                  {'first_name': 'Ольга', 'id': 622170942, 'last_name': 'Савченкова',
#                                   'bdate': '20.12'}]}}
# a = [i['first_name'] for i in data['my_friends']['items']]
# for i in sorted(a):
#     print(i)

# a = input()
# b = input()
# if sorted(a) == sorted(b):
#     print("YES")
# else:
#     print("NO")


# m = {'a': '•—', 'b': '—•••', 'c': '—•—•', 'd': '—••',
#      'e': '•', 'f': '••—•', 'g': '——•', 'h': '••••',
#      'i': '••', 'j': '•———', 'k': '—•—', 'l': '•—••',
#      'm': '——', 'n': '—•', 'o': '———', 'p': '•——•',
#      'q': '——•—', 'r': '•—•', 's': '•••', 't': '—',
#      'u': '••—', 'v': '•••—', 'w': '•——', 'x': '—••—',
#      'y': '—•——', 'z': '——••'}
# b = []
# a = input().lower()
# a = list(a)
# for i in a:
#     b.append(m.get(i))
# for i in b:
#     if i == None:
#         print()
#     else:
#         print(i, end=' ')

# persons = [
#     ('Allison Hill', 334053, 'M', '1635644202'),
#     ('Megan Mcclain', 191161, 'F', '2101101595'),
#     ('Brandon Hall', 731262, 'M', '6054749119'),
#     ('Michelle Miles', 539898, 'M', '1355368461'),
#     ('Donald Booth', 895667, 'M', '7736670978'),
#     ('Gina Moore', 900581, 'F', '7018476624'),
#     ('James Howard', 460663, 'F', '5461900982'),
#     ('Monica Herrera', 496922, 'M', '2955495768'),
#     ('Sandra Montgomery', 479201, 'M', '5111859731'),
#     ('Amber Perez', 403445, 'M', '0602870126')
# ]
# a = {}
# for i in persons:
#     s = dict(salary=i[1], gender=i[2], passport=i[3])
#     a[i[0]] = s
# print(a)

# people = [
#     ['Amy Smith', '694.322.8133x22426'],
#     ['Brian Shaw', '593.662.5217x338'],
#     ['Christian Sharp', '118.197.8810'],
#     ['Sean Schmidt', '9722527521'],
#     ['Thomas Long', '163.814.9938'],
#     ['Joshua Willis', '+1-978-530-6971x601'],
#     ['Ann Hoffman', '434.104.4302'],
#     ['John Leonard', '(956)182-8435'],
#     ['Daniel Ross', '870-365-8303x416'],
#     ['Jacqueline Moon', '+1-757-865-4488x652'],
#     ['Gregory Baker', '705-576-1122'],
#     ['Michael Spencer', '(922)816-0599x7007'],
#     ['Austin Vazquez', '399-813-8599'],
#     ['Chad Delgado', '979.908.8506x886'],
#     ['Jonathan Gilbert', '9577853541']
# ]
#
# phone_book = {key[1]: key[0] for key in people}
# print(phone_book)

# my_tuple = (
# 32, 45, 32, 60, 43, 19, 39, 75, 50, 12, 53, 13, 28, 70, 68, 5, 64, 55, 30, 47, 23, 20, 17, 36, 45, 31, 46, 50, 33, 45,
# 9, 41, 12, 57, 40, 43, 47, 51, 56, 54, 40, 30, 37, 23, 43, 66, 64, 27, 44, 75, 51, 2, 19, 72, 30, 8, 29, 43, 7, 73, 34,
# 65, 54, 50, 43, 6, 50, 45, 49, 30, 39, 50, 41, 70, 38, 16, 31, 51, 72, 45, 58, 39, 50, 56, 24, 30, 9, 53, 27, 31, 68,
# 56, 26, 39, 34, 50, 10, 12, 3, 27)
# my_tuple = list(my_tuple)
# # my_tuple.reverse()
# # my_tuple = tuple(my_tuple)
# # print(my_tuple)

# lonely = 777,
# print(lonely)

# my_tuple = (
# -214, 181, -139, 448, -664, -66, 213, 832, 717, -462, -924, -706, -85, -244, -222, -340, -482, -518, -781, 759, -593,
# 905, -354, -377, -141, -742, 383, -381, 109, -639, -480, -810, -686, 892, -612, 696, 993, 791, 631, -493, -218, -829,
# -275, 619, -628, -241, -565, -835, -69, 747, 711, -252, -811, -407, -153, 904, 933, -254, 307, -493, -419, -109, -543,
# 155, -127, 613, -452, -459, 856, 562, 333, -66, -77, -598, -779, -278, 867, 321, -20, -415, -357, 735, -906, -14, -370,
# 453, -630, -736, -830, -917, 32, 422, -895, 198, 284, 472, -986, -964, -73, 29)
#
# a = [i for i in my_tuple if i % 2 != 0]
# a = sum(a)/len(a)
# print(a)

# a = int(input())
# b = int(input())
# c = tuple(range(a, b+1))
# print(c)

# n = int(input())
# a = range(n, n**2 + 1)
# c = [i for i in a if i % 2 != 0]
# print(tuple(c))

# a = set(map(int, input().split()))
# b = set(map(int, input().split()))
# c = (a & b)
# print(*a - c)
#
# a = set(map(int, input().split()))
# b = set(map(int, input().split()))
# c = (a & b)
# print(*sorted(a - c))


# def say_hello_world(name):
#     print(name + " говорит hello world!")
# name = input()
# say_hello_world(name)


# def summa_n(t):
#     s = sum(range(t + 1))
#     print("Я знаю, что сумма чисел от 1 до " + str(t) + " равна " + str(s))
#
#
# summa_n(int(input()))

'''DEF'''


# def check_password(a):
#     digit = 0
#     up = 0
#     spec = 0
#
#     for i in a:
#         if i.isdigit():
#             digit += 1
#         if i.isupper():
#             up += 1
#         if i in "!@#$%*":
#             spec += 1
#     if digit >= 3 and up > 0 and spec > 0 and len(a) >= 10:
#         print('Perfect password')
#     else:
#         print('Easy peasy')
#
#
# a = input()
# check_password(a)

# def count_letters(a):
#     K = 0
#     N = 0
#     for i in a:
#         if i.isupper():
#             K += 1
#         if i.islower():
#             N += 1
#     print('Количество заглавных символов: ', K)
#     print('Количество строчных символов: ', N)
#
#
# count_letters(input())

# def first_unique_char(a):
#     for i in a:
#         q = a.count(i)
#         if q <= 1:
#             g = a.find(i)
#             return g
#     return -1
#
#
# b = input()
# print(first_unique_char(b))

# def domain_name(m):
#     m = ''.join(m)
#     print(len(m), type(m))
#     if m in 'h':
#         return m[6:]
#     else:
#         return 'WTF'
#
#
# n = input()
# print(domain_name(n))


# def shift_letter(letter: str, shift: int) -> str:
#     """Функция сдвигает символ letter на shift позиций"""
#     a = ord(letter)
#     a += int(shift) % 26
#     if 97 < a < 122:
#         return chr(a)
#     elif a < 97:
#         return chr(123 - (97 - a))
#     elif a > 122:
#         return chr(97 + (a - 123))
#
# 
# letter, shift = map(str, input().split())
# shift = int(shift)
# print(shift_letter(letter, shift))
#
#
# def caesar_cipher()

# MIN_DRIVING_AGE = 18


# def allowed_driving(name, age):
#     if age < MIN_DRIVING_AGE:
#         print(name, 'еще рано садиться за руль')
#     else:
#         print(name, 'может водить')
#
#
# allowed_driving('tim', 17)
# allowed_driving('bob', 18)


# a, b, *c = range(5)
# print(c)


# def count_args(*args):
#     s = 0
#     for i in args:
#         s += 1
#     return s
#
#
# print(count_args(1, 2, 2, 3, 5, 2))

# def only_one_positive(*args):
#     if args == ():
#         return False
#     s = 0
#     for i in args:
#         if i == abs(i):
#             s += 1
#     if s > 1 and str(args) in '0':
#         return False
#     else:
#         return True
#
#
# print(only_one_positive(-1, 0, -3, 5, -3))


# def file_read(file_name):
#     f = open(file_name, encoding='utf-8')
#     print(f.read())
#     f.close()
#
# file_read('kek.txt')

# def create_file_with_numbers(n):
#     with open(f"range_{n}.txt","w") as f:
#         [f.write(str(i)+"\n") for i in range(1, n+1)]
#
#
# create_file_with_numbers(4)

# def longest_word_in_file(file_name):
#     file = open(file_name, 'r', encoding='utf-8')
#     max_world = ''
#     for line in file:
#         words = line.split()
#         for word in words:
#             word_without_punc = remove_punctuation(word)
#             if len(word_without_punc) >= len(max_world):
#                 max_world = word_without_punc
#     file.close()
#     return max_world
#
#
# def remove_punctuation(word):
#     from string import punctuation
#     for punc in punctuation:
#         if punc in word:
#             word = word.replace(punc, '')
#     return word

# import json
# with open('my.json', 'r') as file:
#     data = json.load(file)

# import json
#
# maxim = 0
# maxim_name = ''
# maxim_last = ''
# with open('manager_sales.json', 'r') as file:
#     data = json.load(file)
#
# for i in data:
#     price = 0
#     first = i['manager']['first_name']
#     last = i['manager']['last_name']
#     for a in i['cars']:
#         price += a['price']
#     # print(first, last, price)
#     if price > maxim:
#         maxim = price
#         maxim_last = last
#         maxim_name = first
# print(maxim_name, maxim_last, maxim)

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# a = list(map(lambda x: x ** 2, numbers))
# b = list(map(lambda x: x ** 3, numbers))
# print(a, b, sep='\n')

# print(*[list(map(func, numbers)) for func in [lambda x: x**2, lambda x: x**3]], sep='\n')

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(list(filter(lambda x: x % 2 == 0, numbers)))

# numbers = [54, 71, 65, 51, 36, -82, -32, 61, -61, 92, 17, -68, -62, 40, 16, -49, -51, -38, 60, -24, -61, 3, -26, -46,
#            -97, -28, 36, 7, 52, 56, -96, -69, 67, 76, 16, 36, 38, 74, 11, -87, 69, 69, -69, -61, 92, 67, -45, -26, 94,
#            38, 27, -26, 10, 55, 28, -81, 53, -75, -32, -83, 38, 83, -40, -51, 88, 28, 76, 25, 84, -79, -69, -65, 6, 12,
#            81, -58, -92, 44, -41, 60, -14, -65, 7, 64, -40, -25, -91, -23, -19, -40, -4, 36, 38, 28, -27, -28, 72, 47]

# a = list(filter(lambda x: x < 0, numbers))
# b = list(filter(lambda x: x == 0, numbers))
# c = list(filter(lambda x: x > 0, numbers))
# print(len(a), len(b), len(c))

# print(*[len(list(filter(fnc, numbers))) for fnc in [lambda x: x < 0, lambda x: x == 0, lambda x: x > 0]])

# days = ['One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Eleven', 'Twelve']
# print(*sorted(list(filter(lambda x: len(x) == 4 or x[0] == 'S', days))), sep='\n')

# subject_marks = [('English', 88), ('Science', 90), ('Maths', 97), ('Physics', 93), ('History', 82)]
# [print(*i) for i in sorted(subject_marks, key=lambda x: x[1])]


# subject_marks = [('English', 88), ('Science', 90), ('Maths', 97),
#                  ('Physics', 93), ('History', 82), ('French', 78),
#                  ('Art', 58), ('Chemistry', 76), ('Programming', 91)]
# [print(*i) for i in sorted(subject_marks, key=lambda x: (-x[1], x[0]))]

# models = [{'make': 'Nokia', 'model': 216, 'color': 'Black'},
#           {'make': 'Mi Max', 'model': 2, 'color': 'Gold'},
#           {'make': 'Samsung', 'model': 7, 'color': 'Blue'},
#           {'make': 'Apple', 'model': 10, 'color': 'Silver'},
#           {'make': 'Oppo', 'model': 9, 'color': 'Red'},
#           {'make': 'Huawei', 'model': 4, 'color': 'Grey'},
#           {'make': 'Honor', 'model': 3, 'color': 'Black'}]
#
# [print('Производитель: ' + i['make'] +', модель: ' + str(i['model']) +', цвет: ' + i['color']) for i in sorted(models, key=lambda x: x['color'])]


# from datetime import date
# date_7_08_1996 = date(year=1996, month=8, day=7)
# date_31_12_1981 = date(year=1981, month=12, day=31)
# print(date_7_08_1996)
# print(date_31_12_1981)

# d = int(input())
# m = int(input())
# y = int(input())
# a = date(year=y, month=m, day=d)
# print(a)

# from datetime import date
#
# my_date = date(2013, 6, 21)
# print(my_date.month, my_date.year)

# from datetime import date
#
# d = 20
# m = 10
# y = 1998
# user_date = date(y, m, d)
# print(user_date)
# print(f'{user_date.day:02d}', f'{user_date.month:02d}', f'{user_date.year:04d}', sep='.')

# a = int(input())
# b = int(input())
# print(f'Точка(x = {a}, y = {b})')

# number_pi = 3.141592653589793
# print(f'{number_pi = :.6f}')

# a = float(input())
# print(f'{a:.2f}')

# n = 12345678912345
#
# print(f'{n:,d}')
# print(f'{n:_d}')
#
# sep = '_'
# print(f'{n:{sep}d}') # вложенная f-строка

# print(f'Число Квадрат Куб')
# for x in range(1, 11):
#    print(f'{x} {x*x} {x*x*x}')
#
# # А теперь с выравниванием
#
# print(f'Число\t\tКвадрат\t\tКуб')
# for x in range(1, 11):
#    print(f'{x:2d}\t\t{x*x:3d}\t\t{x*x*x:4d}')
#
# a = int(input())
# print(f'{a:010d}')


# APPLES = .50
# BREAD = 1.50
# CHEESE = 2.25
# num_apples = 3
# num_bread = 10
# num_cheese = 6
# price_apples = num_apples * APPLES
# price_bread = num_bread * BREAD
# price_cheese = num_cheese * CHEESE
# str_apples = 'Яблоки'
# str_bread = 'Хлеб'
# str_сheese = 'Сыр'
# total = price_bread + price_cheese + price_apples
# print(f'{"Список покупок":^30s}')
# print(f'{"=" * 30}')
# print(f'{str_apples:10s}{num_apples:10d}\t${price_apples:>5.2f}')
# print(f'{str_bread:10s}{num_bread:10d}\t${price_bread:>5.2f}')
# print(f'{str_сheese:10s}{num_cheese:10d}\t${price_cheese:>5.2f}')
# print(f'{"Total:":>20s}\t${total:>5.2f}')


# from datetime import date
# print(date.min)
#
# a = date(2015, 8, 21)
# print(a.min)

# hello = 'Hello World!'
# print(type(hello))
#
# my_list = [2, 4, 43]
# print(type(my_list))
#
# print(type(True))
# print(type(3))
# print(type(6 / 3))
#
# print(hello, 'Это строка?', isinstance(hello, str))


# class Car:
#     """Класс для определения характеристик машин"""
#     pass
#
#
# print(Car.__doc__)  # Результат: Класс для определения характеристик машин


# class Contact:
#     name = 'Barak'
#     phone_number = '+1 202 345 4564'
#
#
# print(Contact.__dict__)
# print(getattr(Contact, 'name'))
