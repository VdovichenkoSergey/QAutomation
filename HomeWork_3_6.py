
def ReturnFloat():

    '''функция попросит ввести число. Пока он не введёт правильно, просите
    его ввести. Функция возвращает введённое число.'''

    rep = input('Input digit: ')
    while True:
        try:
            return float(rep)
        except ValueError:
            rep = input('Input digit only: ')


def ReturnStr():

    '''которая попросит пользователя ввести слово (строка без пробелов в
    середине, а вначале и в конце пробелы могут быть). Пока он не введёт правильно, просите
    его ввести. Функция возвращает введённое слово.'''


    s = input('Input Word: ')

    while True:
        s1 = s.strip()
        if s1.count(' ') == 0:
            return s
            break
        else:
            s = input('input Word without spaces in the center: ')
            continue


def is_year_leap(year):
    '''принимающую 1 аргумент — год, и возвращающую True,
    если год високосный, и False иначе.'''
#    year = input("Input year which will be checked: ")

    while True:
        try:
            year = int(year)
            if year % 4 == 0 and year % 100 != 0 or year % 400 == 0 or year != 0:
                return True
                break
            else:
                return False
                break
        except ValueError:
            year = input("Input integer digit: ")


def triangle(a, b, c):

    '''Функция принимает три числа a, b, c. Функция должна определить,
существует ли треугольник с такими сторонами.
Если треугольник существует, вернёт True, иначе False.'''

    if a + b <= c or c + b <= a or a + c <= b:
        return False
    else:
        return True



def TriangleType(a, b, c):
    '''Функция принимает три числа a, b, c. Функция должна определить, существует ли
треугольник с такими сторонами и если существует, то возвращает тип треугольника
Equilateral triangle (равносторонний), Isosceles triangle (равнобедренный), Versatile triangle
(разносторонний) или не треугольник (Not a triangle).'''

    while True:
        try:
            a = int(a)
            b = int(b)
            c = int(c)
            if triangle(a, b, c) == False:
                return 'Not a triangle'
                break
            if a == b == c:
                return 'Equilateral triangle'
                break
            if a == b != c or a == c != b or c == b != a:
                return 'Isosceles triangle'
                break
            if a != b != c:
                return 'Versatile triangle'
                break
        except ValueError:
            a = input('input only integer digit for first parameter: ')
            b = input('input only integer digit for first parameter: ')
            c = input('input only integer digit for first parameter: ')
            continue



def distance(x1, y1, x2, y2):
    '''Даны четыре действительных числа: x1, y1, x2, y2. Напишите функцию distance(x1, y1, x2,
y2), вычисляющую расстояние между точками с координатами (x1, y1) и (x2, y2). Считайте
четыре действительных числа от пользователя и выведите результат работы этой функции.'''

    return 'distance between x1 and x2: ', x2 - x1
    return 'distance between y1 and y2: ', y2 - y1
