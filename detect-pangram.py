# https://www.codewars.com/kata/545cedaa9943f7fe7b000048/train/python
from test import Test
import string


def is_pangram(s):
    s = s.lower()
    try:
        for char in string.ascii_lowercase:
            s.index(char)
        return True
    except ValueError:
        return False


pangram = "The quick, brown fox jumps over the lazy dog!"
Test.assert_equals(is_pangram(pangram), True)
