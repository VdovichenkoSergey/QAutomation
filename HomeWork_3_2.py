s = input('Input some string: ')

if len(s) % 2 != 0:
    s1 = s[:len(s) // 2 + 1]
    s2 = s[len(s) // 2 + 1:]

else:
    s1 = s[:len(s) // 2]
    s2 = s[len(s) // 2:]
s3 = (s2 + s1)
print(s3)
