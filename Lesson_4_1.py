def SrtOny(a):
    '''Напишите функцию, которая удаляет все небуквенные символы внутри
строки'''
    a = str(a)
    a1 = ''
    for i in a:
        if i.isalpha() == True and i.isascii() == True:
            a1 = a1 + i

    assert a1.isalpha() is True
    assert a1.isascii() is True
    return a1

x = SrtOny('q1йцуw2e3r4;')
print(x)