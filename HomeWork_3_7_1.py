s = '''We are not what we should be!
We are not what we need to be.
But at least we are not what we used to be
(Football Coach)'''

s1 = s.lower()
l = s1.split()
l1 = []
d = {}
for i in l:
    if i not in l1:
        l1.append(i)

for i in l1:
    d[i] = ''

for i in d:
    d[i] = l.count(i)
print()
print(d)
