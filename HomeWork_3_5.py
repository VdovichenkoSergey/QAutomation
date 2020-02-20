d1 = input('Input digit 1: ')
d2 = input('Input digit 2: ')

try:
    d1 = float(d1)
    d2 = float(d2)

except ValueError:
    d1 = str(d1)
    d2 = str(d2)

print(d1 + d2)
