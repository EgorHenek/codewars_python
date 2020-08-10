# https://www.codewars.com/kata/54521e9ec8e60bc4de000d6c/train/python

from test import Test


def max_sequence(param):
    maxl = 0
    maxg = 0
    for n in param:
        maxl = max(0, maxl + n)
        maxg = max(maxg, maxl)
    return maxg


Test.describe("Tests")
Test.it('should work on an empty array')
Test.assert_equals(max_sequence([]), 0)
Test.it('should work on the example')
Test.assert_equals(max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 4]), 6)
