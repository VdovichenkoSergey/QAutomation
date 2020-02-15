x = 10
while x > 0:
    print(str(x) + '!')
    x-=1

print()
print('task 2')

l = [1, 2, 3, 4, 5]

while len(l) != 0:
    print(l.pop())

print()
print('Task 3')

while True:
    word = input('Input word without spaces: ')
    if word.count(' ') == 0:
        break
    else:
        print(word)

print()
print('Task 4')

while True:
    word = input('Input word without spaces: ')
    if not ' ' in word:
        break


