'''Файл имеет вид таблицы: Фамилия Имя Отдел Зарплата (В первой строке заголовки
колонок)
 Посчитайте сколько отделов на фирме
 Определите максимальную зарплату
 Определите максимальную зарплату в каждом отделе
 Выведите «Отдел Макс_Зарплата Фамилия_человека_с_такой_зарплатой» в
новый файл'''

with open('employee_table.txt', 'r', encoding='utf-8') as table_file:
    keys = table_file.readline().split()
    data = table_file.read().split()
    d = {keys[i]: data[i::len(keys)] for i in range(len(keys))}
    departments = d['Отдел']
    salary = [int(i) for i in d['Зарплата']]

    # print(f'Кол-во отделов: {len(departments)}')
    print(f'salary: {salary}')
    print(f'max salary: {max(salary)}')
    # print(f'departments: {departments}')
    # print(f'data: {data}')
    # print(f'd: {d}')


