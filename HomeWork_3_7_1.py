s = '''We are not what we should be!
We are not what we need to be.
But at least we are not what we used to be
(Football Coach)'''

s1 = s.lower()

l = s1.split()
print(l)
l1 = []
for i in range(len(l)):
    if l[i] not in l1[:]:
        l1.append(l[i])
print(l1)

d = {}
for i in range(len(l1)):
    d = d.update({l1[i]:'none'})
print(d)
