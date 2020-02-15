def enter_number():

'''There is a comment about function destination'''


    while True:
        x = input('Input some digit: ')
        try:
            x = float(x)
            break
        except ValueError as e:
            print('Not a number!!!')
        else:
            break
    return x


m = enter_number()

print(m*2)
