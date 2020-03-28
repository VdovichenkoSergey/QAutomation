# Файл имеет вид таблицы: Фамилия Имя Отдел Зарплата (В первой строке заголовки колонок)
# •	Посчитайте сколько отделов на фирме
# •	Определите максимальную зарплату
# •	Определите максимальную зарплату в каждом отделе
# •	Выведите «Отдел Макс_Зарплата  Фамилия_человека_с_такой_зарплатой» в новый файл
# Подсказка: используйте словари.

with open('table.txt', encoding='utf-8') as input_file:
    with open('table_info.txt', 'w', encoding='utf-8') as output_file:
        keys = input_file.readline().strip().split()
        data = input_file.read().split()
        d = {keys[i]: data[i::len(keys)] for i in range(len(keys))}
        deps = d['Отдел']
        dep_count = len(set(deps))
        print(f'Количество отделов: {dep_count}')
        salary = [int(item) for item in d['Зарплата']]
        print(f'Максимальная зарплата в фирме: {max(salary)}')
        new_dict = {}
        print(f'Отдел Макс_Зарплата Фамилия_человека_с_такой_зарплатой', file=output_file)
        for k in range(len(deps)):
            dep_name = deps[k]
            dep_salary = int(salary[k])
            dep_surname = d['Фамилия'][k]
            if new_dict.get(dep_name) is None or new_dict[dep_name][0] < dep_salary:
                new_dict[dep_name] = [dep_salary, dep_surname]
        for k in new_dict:
            print(k, new_dict[k][0], new_dict[k][1], file=output_file)

