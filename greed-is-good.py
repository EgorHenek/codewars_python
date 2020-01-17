# https://www.codewars.com/kata/5270d0d18625160ada0000e4/train/python
from test import Test


def score(dice):
    counts = {x: 0 for x in range(1, 7)}
    result = 0

    for n in dice:
        counts[n] += 1
    for x, n in counts.items():
        if n >= 3 and x == 1:
            result += 1000
            result += (n - 3) * 100
        elif n >= 3:
            result += x * 100
            if x == 5:
                result += (n - 3) * 50
        elif x == 1:
            result += n * 100
        elif x == 5:
            result += n * 50
    return result


Test.describe("Example Tests")
Test.it("Example Case")
Test.assert_equals(score([2, 3, 4, 6, 2]), 0)
Test.assert_equals(score([4, 4, 4, 3, 3]), 400)
Test.assert_equals(score([2, 4, 4, 5, 4]), 450)
