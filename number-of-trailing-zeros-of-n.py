# https://www.codewars.com/kata/52f787eb172a8b4ae1000a34/train/python
from math import log

from test import Test


def zeros(n):
    if n == 0:
        return 0

    count = 0
    for i in range(int(log(n, 5))):
        count += n // 5 ** (i + 1)
    return count


Test.describe("Sample Tests")
Test.it("Should pass sample tests")
Test.assert_equals(zeros(0), 0, "Testing with n = 0")
Test.assert_equals(zeros(6), 1, "Testing with n = 6")
Test.assert_equals(zeros(30), 7, "Testing with n = 30")
