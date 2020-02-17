title1 = 'Exercise 2.1'
k1 = 158
k2 = 971

from math import sqrt
g = sqrt(k1**2 + k2**2)

print()
print(title1)
print()
print('Гипотенуза треугольника: ', g)
print()

title2 = 'Exercise 2.2'

print(title2)
print()

x = input('Введите двухзачное число: ')

print()
print(int(x) // 10)
print()

title3 = 'Exercise 2.3'
print(title3)
print()

y = input('Введите трехзначное число: ')
z = list(y)
a = int(z[0])
b = int(z[1])
c = int(z[2])
print()
print('Digits sum: ', a + b + c)
print()

title4 = 'Exercise 2.4'
print(title4)
print()

n = int(input('Введите целое число: '))
print('Следующее четное число: ', n // 2 * 2 + 2)
print()


title5 = 'Exercise 2.5'
print(title5)
print()

float1 = float(input("Введите положительное дробное число: "))
print('Дробная часть: ', float1 - int(float1))
print()

title6 = 'Exercise 2.6'
print(title6)
print()

x = float(input("Введите положительное дробное число: "))
print('Первая цифра после точки: ', int(x * 10) % 10)
print()

