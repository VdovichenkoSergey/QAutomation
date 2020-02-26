def second_value_method2(*x):

    l = list(set(x))
    l.sort() # не уверен, но вроде и так уже отсортировано
    return l

a = second_value_method2(8, 2, 8, 2, 4, 1, 0, 3)
print(a)
