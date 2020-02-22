l = ['qwe', 'qwer', 'qwer']
a = 0

for i in l:
    if len(i) % 2 != 0:
        a += 1
print(a)


d = {1: 'name', 2: 'qwe', 3: 'rty'}

for i in d:
    print(i, d[i], type(d[i]))
