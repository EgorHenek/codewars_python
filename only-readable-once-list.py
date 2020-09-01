# https://www.codewars.com/kata/53f17f5b59c3fcd589000390/solutions/python
from test import Test


class SecureList:
    def __init__(self, values: list):
        self.values = values[:]

    def __getitem__(self, item):
        return self.values.pop(item)

    def __len__(self):
        return len(self.values)

    def __repr__(self):
        return self._print()

    def __str__(self):
        return self._print()

    def _print(self):
        values = self.values
        self.values = []
        return f"[{', '.join(map(str, values))}]"


base = [1, 2, 3, 4]
a = SecureList(base)

Test.assert_equals(a[0], base[0], "List returned wrong value.")
Test.assert_equals(a[0], base[1], "List returned wrong value.")
Test.assert_equals(len(a), 2, "List hasn't deleted it's items once accessed")
print("current List: %s" % a)
Test.assert_equals(len(a), 0, "List Should be empty after printing")
a = SecureList(base)
print("current List: %r" % a)
Test.assert_equals(len(a), 0,
                   "List Should be empty after printing a representation")
