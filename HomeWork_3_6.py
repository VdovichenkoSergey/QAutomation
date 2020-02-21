'''print('Task 6.1')
print()

def ReturnFloat():

    функция попросит ввести число. Пока он не введёт правильно, просите
    его ввести. Функция возвращает введённое число.

    rep = input('Input digit: ')
    while True:
        try:
            print(float(rep))
            break
        except ValueError:
            rep = input('Input digit only: ')


x = repeat()
print(x)
print()


print('Task 6.2')
print()

def ReturnStr():

    которая попросит пользователя ввести слово (строка без пробелов в
    середине, а вначале и в конце пробелы могут быть). Пока он не введёт правильно, просите
    его ввести. Функция возвращает введённое слово.


    s = input('Input Word: ')

    while True:
        s1 = s[1:-1]
        if s1.count(' ') == 0:
            print(s)
            break
        else:
            s = input('input Word without spaces in the center: ')

test = ReturnStr()
print(test)
print()'''

print('Task 6.3')
print()

def is_year_leap():
    '''принимающую 1 аргумент — год, и возвращающую True,
    если год високосный, и False иначе.'''
    year = input("Input year which will be checked: ")

    while True:
        try:
            year = int(year)
            if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
                print('True')
                break
            else:
                print('Else')
                break
        except ValueError:
            year = input("Input integer digit: ")
year = is_year_leap()
print(year)
