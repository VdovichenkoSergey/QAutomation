# res = [x**(1/2) for x in range(1, 26, 2)]
#
# print(res)

# Task 5.1

res1 = [2**n for n in range(0, 21)]
# print(res1)

# Task 5.2

l = [5, 7, 9, 11]
res2 = [i % 3 for i in l]
# print(res2)

l1 = [3, 5.4, 'qwe', (11, 12)]
res3 = [i for i in l1 if i]
print(res3)