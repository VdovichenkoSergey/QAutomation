def front_x(*words):

    '''Если дан список строк, вернуть список со строками
    в отсортированном порядке, за исключением группировки всех строк, начинающихся с «x».'''

    l = list(words)
    l1 = []
    a = 0
    for i in l:
        if i[0] == 'x':
            l1.append(i)
            l.remove(i)


    print(l)
    print(l1)
    # return l


# print('\n', 'front_x')
y = front_x('bbb', 'ccc', 'axx', 'xzz', 'xaa')
print(y)
#      ['xaa', 'xzz', 'axx', 'bbb', 'ccc'])
# test(front_x(['ccc', 'bbb', 'aaa', 'xcc', 'xaa']),
#      ['xaa', 'xcc', 'aaa', 'bbb', 'ccc'])
# test(front_x(['mix', 'xyz', 'apple', 'xanadu', 'aardvark']),
#      ['xanadu', 'xyz', 'aardvark', 'apple', 'mix'])
