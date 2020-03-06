class Rectangle:

    def __init__(self, side1, side2):
        self.side1 = side1
        self.side2 = side2

    def square(self):
        return f'Rectangle square: {self.side1 * self.side2}'

    def perimeter(self):
        return f'Rectangle perimeter: {self.side1 + self.side2 + self.side1 + self.side2}'

    def __str__(self):
        message = f'Rectangle parameters (cm): \n \n' \
                  f'Side a: {self.side1} \n' \
                  f'Side b: {self.side2} \n' \
                  f'Side c: {self.side1} \n' \
                  f'Side d: {self.side2} \n'
        return message


a = Rectangle(2, 3)

print('\n', a)
print(a.square(), '\n')
print(a.perimeter(), '\n')

