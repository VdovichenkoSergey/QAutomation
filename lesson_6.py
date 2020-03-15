fw = open('D:/vdovichenko/test.txt', 'a')
fw.write('adasas')

fw.close()

fr = open('D:/vdovichenko/test.txt', 'r')
print(fr.read())

fr.close()
print()

fline = open('D:/vdovichenko/test.txt', 'r')

for line in fline:
    print(f'{line.rstrip()}!', end='\n') # выводим каждую строку с ! в конце
                                         # (убирая лишние пробелы и делая вывод с новой строки)
fline.close()

print_to_file = open('D:/vdovichenko/test.txt', 'a')
print('New line', file=print_to_file)

print_to_file.close()



