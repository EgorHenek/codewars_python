# https://www.codewars.com/kata/5390bac347d09b7da40006f6/train/python

from test import Test


def to_jaden_case(string):
    return ' '.join(map(str.capitalize, string.split()))



quote = "How can mirrors be real if our eyes aren't real"
Test.assert_equals(to_jaden_case(quote), "How Can Mirrors Be Real If Our Eyes Aren't Real")
