# Fill in the Line class methods to accept coordinates as a pair of tuples and return the slope and distance of the line.
class Line:

    def __init__(self, coor1, coor2):
        (x1, y1) = coor1
        (x2, y2) = coor2
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def distance(self):
        return (((self.x2 - self.x1) ** 2) + ((self.y2 - self.y1) ** 2)) ** 0.5

    def slope(self):
        return (self.y2 - self.y1) / (self.x2 - self.x1)


coordinate1 = (3, 2)
coordinate2 = (8, 10)

li = Line(coordinate1, coordinate2)
print(li.distance())
print(li.slope())
print('\n')
# Fill in the class
class Cylinder:
    pi = 3.14
    def __init__(self, height=1, radius=1):
        self.height = height
        self.radius = radius

    def volume(self):
        return self.pi * self.height * (self.radius ** 2)

    def surface_area(self):
        return (2 * self.pi * self.radius * self.height) + (2 * self.pi * (self.radius ** 2))


c = Cylinder(2, 3)
print(c.volume())
print(c.surface_area())
