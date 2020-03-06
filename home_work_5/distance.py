from math import sqrt


class Distance:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance_from_zero(self):
        return f"Distance from zero: {sqrt(self.x ** 2 + self.y ** 2)}"

    def distance_point_to_point(self, *second_point):
        return f"Distance from point to point: " \
               f"{sqrt((second_point[0] - self.x) ** 2 + (second_point[1] - self.y) ** 2)}"

    def __str__(self):
        return f'{self.x}, {self.y}'


point1 = Distance(3, 5)
point2 = Distance(-5, -11)

print(point1)

print('\n', point1.distance_from_zero(), '\n')
print(point1.distance_point_to_point(point2.x, point2.y))

#print(point1.distance_point_to_point(point2))