# https://www.codewars.com/kata/where-my-anagrams-at/train/python
from test import Test


def anagrams(word, words):
    word = sorted(word)
    return [v for v in words if sorted(v) == word]


Test.assert_equals(anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']), ['aabb', 'bbaa'])
Test.assert_equals(anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']), ['carer', 'racer'])
