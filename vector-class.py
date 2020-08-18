# https://www.codewars.com/kata/532a69ee484b0e27120000b6/train/python
import math

from test import Test as test

class Vector:
    def __init__(self, *args):
        if len(args) == 1:
            args = args[0]
        self.x, self.y, self.z = (args)
    
    def to_tuple(self):
        return (self.x, self.y, self.z)
    
    def __add__(self, vector):
        return Vector(self.x + vector.x, self.y + vector.y, self.z + vector.z)
    
    def __sub__(self, vector):
        return Vector(self.x - vector.x, self.y - vector.y, self.z - vector.z)
    
    @property
    def magnitude(self):
        return math.sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)
    
    def __str__(self):
        return f'<{self.x}, {self.y}, {self.z}>'

    def __eq__(self, vector):
        return self.magnitude == vector.magnitude and self.to_tuple() == vector.to_tuple()

    def _ijk(self, vector):
        i = self.y * vector.z - self.z * vector.y
        j = self.z * vector.x - self.x * vector.z
        k = self.x * vector.y - self.y * vector.x
        return (i, j, k)
    
    def cross(self, vector):
        return Vector(self._ijk(vector))
    
    def dot(self, vector):
        return self.x * vector.x + self.y * vector.y + self.z * vector.z


        


test.describe("Basic tests")

examples = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

test.it("Both initializiations should result in the same vector")
test.assert_equals(Vector(examples[0]), Vector(*examples[0]))
test.it("Should correctly display coordinates")
v = Vector(examples[1])
test.assert_equals(v.x, 4)
test.assert_equals(v.y, 5)
test.assert_equals(v.z, 6)
# test.it("Should correctly calculate magnitude")
# test.assert_approx_equals(Vector(examples[0]).magnitude, 3.741, 0.001)
test.it("Should handle array representation")
test.assert_equals(Vector(examples[2]).to_tuple(), tuple(examples[2]))
test.it("Should handle string representation")
test.assert_equals(str(Vector(examples[1])), "<4, 5, 6>")
test.it("Should handle addition")
test.assert_equals(Vector(examples[0]) + Vector(*examples[1]), Vector(5, 7, 9))
test.it("Should handle subtraction")
test.assert_equals(Vector(examples[0]) - Vector(*examples[2]), Vector(-6, -6, -6))
test.it("Should handle cross product")
test.assert_equals(Vector(examples[0]).cross(Vector(*examples[1])), Vector(-3, 6, -3))
test.it("Should handle dot product")
test.assert_equals(Vector(examples[1]).dot(Vector(*examples[2])), 122)