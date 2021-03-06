def match_ends(*words):
    '''Получив список строк, верните длину каждой строки, где длина строки равна 2 или более и первая
и последние символы строки одинаковы.'''

    l = list(words)
    l1 = []
    d = {}
    for i in l:
        if len(i) > 1 and i[0] == i[-1]:
            d[i] = len(i)
            # l1.append(len(i)) - just length of strings will be returned
    return d

x = match_ends('aba', 'xyz', 'aa', 'x', 'bbb')
# print(x)
# test(match_ends(['', 'x', 'xy', 'xyx', 'xx']), 2)
# test(match_ends(['aaa', 'be', 'abc', 'hello']), 1)

print()

def front_x(*words):

    '''дан список строк, вернуть список со строками в отсортированном порядке,
    за исключением группировки всех строк, начинающихся с «x».'''

    l = list(words)
    lx = []
    lsort = []
    a = 0
    for i in l:
        if i[0] == 'x':
            lx.append(i)
        else:
            lsort.append(i)
    lsort.sort()
    l = lx + lsort

    return l

y = front_x('bbb', 'ccc', 'axx', 'xzz', 'xaa')
print(y)


def sort_last(*tuples):

    '''Given a list of non-empty tuples, return a list sorted in increasing
    order by the last element in each tuple'''

    l = list(tuples)
    l1 = sorted(l, key=lambda x: x[1])

    return l1

z = sort_last((1, 3), (3, 2), (2, 1))
print(z)
#      [(2, 1), (3, 2), (1, 3)])
# test(sort_last([(2, 3), (1, 2), (3, 1)]),
#      [(3, 1), (1, 2), (2, 3)])
# test(sort_last([(1, 7), (1, 3), (3, 4, 5), (2, 2)]),
#      [(2, 2), (1, 3), (3, 4, 5), (1, 7)])