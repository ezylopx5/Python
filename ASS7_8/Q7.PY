import math

class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def magnitude(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def rotate_x(self):
        return math.atan2(self.y, self.x)

    def distance(self, other):
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)

class Vector3D(Vector2D):
    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.z = z

    def magnitude(self):
        return math.sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)

v2d = Vector2D(3, 4)
v3d = Vector3D(3, 4, 5)

print("Magnitude of 2D Vector:", v2d.magnitude())
print("Magnitude of 3D Vector:", v3d.magnitude())