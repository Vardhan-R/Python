import math

class Vector:
    def __init__(self, x, y, z = 0):
        self.x = x
        self.y = y
        self.z = z

    def mult(self, a):
        return Vector(a * self.x, a * self.y, a * self.z)

    def mag(self):
        return math.sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)

    def magSq(self):
        return self.x ** 2 + self.y ** 2 + self.z ** 2

    def normalise(self):
        if self.mag() != 0:
            return self.mult(1 / self.mag())

    def setMag(self, m):
        return Vector(self.x / self.mag(), self.y / self.mag(), self.z / self.mag()).mult(m)

    def dir(self): # z = 0
        return(math.atan2(self.y, self.x))

    def setDir(self, t): # z = 0
        return Vector(self.mag() * math.cos(t), self.mag() * math.sin(t), self.z)

    def rotate(self, t): # z = 0
        return Vector(self.mag() * math.cos(self.dir() + t), self.mag() * math.sin(self.dir() + t), self.z)

def add(a, b):
    return Vector(a.x + b.x, a.y + b.y, a.z + b.z)

def sub(a, b):
    return Vector(a.x - b.x, a.y - b.y, a.z - b.z)

def dot(a, b):
    return a.x * b.x + a.y * b.y + a.z * b.z

def cross(a, b):
    return Vector(a.y * b.z - a.z * b.y, a.z * b.x - a.x * b.z, a.x * b.y - a.y * b.x)

def distBetween(a, b):
    return Vector(a.x - b.x, a.y - b.y, a.z - b.z).mag()

def angBetween(a, b):
    return math.acos(dot(a, b) / (a.mag() * b.mag()))