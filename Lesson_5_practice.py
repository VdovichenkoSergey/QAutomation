# class Test:
#     def cotenation(self):
#         return self.name + ' ' + self.surname
#
# user = Test()
# user1 = user.cotenation('Vic', 'Cacul')
# print(user1)

class Rectangle:
    def __init__(self, line1, line2):
        self.x = line1
        self.y = line2

    def squre(self):
        return 'Square: ', self.x * self.y

    def perimetr(self):
        return 'SUM: ', self.x + self.x + self.y + self.y

rect = Rectangle(5, 6)
print(*rect.squre())
print(*rect.perimetr())