# Записывает в новый файл все слова в алфавитном порядке из другого файла с текстом.
# Каждое слово на новой строке.
# * (доп.) Рядом со словом укажите сколько раз оно встречалось в тексте
import string
with open('1.txt') as input_file:
    with open('4.txt', 'w') as output_file:
        s = input_file.read().lower()
        s = "".join(l for l in s if l not in string.punctuation)
        l = s.split()
        for item in sorted(set(l)):
            print(f'{item}: {l.count(item)}', file=output_file)
