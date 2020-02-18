s = input('Input some string: ')
s1 = s[:len(s) // 2]
s2 = s[len(s) // 2:]

if len(s) % 2 != 0:
    s1 = s[:len(s) // 2]
    s2 = s[len(s) // 2:]
    print(s2, s1)
else:
    s1 = s[:len(s) // 2]
    s2 = s[len(s) // 2:]
    print(s2, s1)
