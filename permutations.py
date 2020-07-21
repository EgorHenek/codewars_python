# https://www.codewars.com/kata/5254ca2719453dcc0b00027d/train/python
import itertools

from test import Test


def permutations(string: str) -> map:
    return map(''.join, set(itertools.permutations(string)))


Test.assert_equals(sorted(permutations('a')), ['a'])
Test.assert_equals(sorted(permutations('ab')), ['ab', 'ba'])
Test.assert_equals(sorted(permutations('aabb')),
                   ['aabb', 'abab', 'abba', 'baab', 'baba', 'bbaa'])
