# https://www.codewars.com/kata/5552101f47fc5178b1000050/train/python
from test import Test


def dig_pow(n, p):
    summary = 0
    for x in str(n):
        summary += int(x) ** p
        p += 1
    result = summary / n
    if result.is_integer():
        return result
    return -1


Test.assert_equals(dig_pow(89, 1), 1)
Test.assert_equals(dig_pow(92, 1), -1)
Test.assert_equals(dig_pow(46288, 3), 51)
