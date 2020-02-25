print('method 1')
print()
s = input('input some string: ')

try:
    list1 = [s[2], s[-2], s[:5], s[:-2], s[1::2], s[::2], s[::-1], s[::-2], s[-2::-2], s[-2:0:-1], len(s)]
    for i in list1:
        print(list1[i])
except IndexError:
    print('your string too small, input string with 3 symbols or more: ')
print()


print('method 2')
print()

s = input('input some string: ')

while True:
    try:
        print(s[2], s[-2], s[:5], s[:-2], s[1::2], s[::2], s[::-1], s[::-2], s[-2::-2], s[-2:0:-1], len(s), sep='\n')
        break
    except IndexError:
        s = input('your string too small, input string with 3 symbols or more: ')
