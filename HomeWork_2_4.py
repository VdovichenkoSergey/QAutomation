a = int(input('Введите сторону а: '))
b = int(input('Введите сторону b: '))
c = int(input('Введите сторону c: '))

if a + b <= c or c + b <= a or a + c <= b:
    print('Not a triangle')
else:
    print('It is a triangle')
