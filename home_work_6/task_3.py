from itertools import groupby

'''Записывает в новый файл все слова в алфавитном порядке из другого файла с
текстом. Каждое слово на новой строке.
Рядом со словом укажите сколько раз оно встречалось в тексте'''

with open('task3_output.txt', 'r') as file_output:
    with open('task3_input.txt', 'w') as file_input:

        output_temp = file_output.read().lower().split()
        l = [i.strip("!'.','?") for i in output_temp]
        l1 = list(set(l))
        l1.sort()

        for i in l1:
            print(f'{i} {l.count(i)}', file=file_input)




