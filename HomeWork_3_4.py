print('Task 4.1')
print()

l = [11, 22, 33, 'center', 44, 55, 66, 77]

while len(l) > 0:
    print(l.pop(0))

print()
print('Current length of list: ', len(l))
print()


print('Task 4.2')
print()

s = 'qwertyuiop'

while len(s) > 0:
    print(s[0])
    s = s[1:]
print()


print('Task 4.3')
print()

l1 = [34, 22, 33, 12, 1, 77, 15]

while len(l1) > 0:
    l1.sort()
    print(l1.pop(0))
print()


print('Task 4.4')
print()

l2 = [2, 1, 1, 2, 2, 2, 2, 2, 2, 11, 2, 3, 3, 3, 3, 3]
number = 1
max1 = 1

for i in range(len(l2) - 1):
    if l2[i] == l2[i + 1]:
        number += 1
    if l2[i] != l2[i + 1]:
        number = 1
    if max1 < number:
        max1 = number
print()
print(max1)
