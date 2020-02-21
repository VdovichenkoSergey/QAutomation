s = '''We are not what we should be!
We are not what we need to be.
But at least we are not what we used to be
(Football Coach)'''
l = s.split()
print(s)
print()
print(l)
print()

print('Number of words in the text: ', len(l))
print()

for i in range(len(l)):
    l[i] = l[i].strip("!'.','?'(')'")
print(l)
print()

l.sort(key=str.lower)
print(l)
