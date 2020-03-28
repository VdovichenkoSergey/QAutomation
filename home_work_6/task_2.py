from HomeWork_4_1 import la_la

'''Записать в текстовый файл и вашу песню “la-la-la”'''

lala_file = open('c:/git/QAutomation/home_work_6/lala_file.txt', 'w')
lala_file.write(la_la(4, 5, 1))
lala_file.close()

lala_file = open('c:/git/QAutomation/home_work_6/lala_file.txt', 'r')
print(lala_file.read())
lala_file.close()

'''Прочитать и вывести на экран код файла, в котором вы создавали класс Person'''

person_file = open('../Profile/Person.py', 'r', encoding='utf-8')
print(person_file.readlines())
person_file.close()

'''считываем построчно строки из файла и выводим строки,
добавляя в конец этих строк восклицательный знак'''

iter_file = open('iteration_file.txt', 'r')

for line in iter_file:
    print(f'{line.rstrip()}!')
iter_file.close()

'''Записываем “Number: строка из файла” из одного файла в другой. Не
забываем закрывать файлы'''

temp_file = open('../home_work_6/temp.txt', 'r')
number_file = open('c:/git/QAutomation/home_work_6/number_file.txt', 'w')
n_line = 0

for line in temp_file:
    n_line += 1
    print(f'{n_line}: {line.strip()}', file=number_file)

temp_file.close()
number_file.close()


def convert_to_digits(file_path):

    '''Напишите программу, которая пытается преобразовать текст из файла в
    число. Файл должен все равно закрываться в блоке finally. Если
    преобразование удалось (в блоке else) – выводится сообщение «I did it!»'''

    with open(file_path, 'r') as file_read:
        temp_data = file_read.read()

        try:
            temp_data = int(temp_data)
            return 'I did it!'
        except:
            return 'Conversion is impossible'
        finally:
            file_read.close()


x = convert_to_digits('../home_work_6/digits_only.txt')
print(x)



