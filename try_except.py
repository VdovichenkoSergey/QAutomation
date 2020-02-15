

'''
s = input('enter value: ')

try:
    s = int(s)
except:
    print('Error')
'''
print()
print('Task 2')


while True:
    x = input('Input some digit: ')
    try:
        x = float(x)
        break
    except ValueError as e:
        print('Not a number!!!')
    else:
        break


print(type(x))

