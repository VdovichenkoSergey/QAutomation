from math import sqrt


class Distance:
    def __init__(self, x1=0, y1=0, x2=0, y2=0):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2

    def dist(self):
        d = sqrt(((self.x2 - self.x1) ** 2) + ((self.y2 - self.y1) ** 2))
        return d

# dis = Distance()
# print(dis.dist())
