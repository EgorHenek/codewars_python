# https://www.codewars.com/kata/5838b5eb1adeb6b7220000f5/train/python
from itertools import chain
from collections import defaultdict

from test import Test as test


def id_best_users(*args):
    every_months_buyers = set(args[0])
    result = defaultdict(list)
    summary = list(chain.from_iterable(args))

    for buyers in args:
        every_months_buyers = every_months_buyers & set(buyers)

    for buyer in every_months_buyers:
        result[summary.count(buyer)].append(buyer)
    return sorted([[count, sorted(value)] for count, value in result.items()],
                  reverse=True,
                  )


test.describe("Basic Tests")

a1 = ['A042', 'B004', 'A025', 'A042', 'C025']
a2 = ['B009', 'B040', 'B004', 'A042', 'A025', 'A042']
a3 = ['A042', 'A025', 'B004']
test.assert_equals(id_best_users(a1, a2, a3),
                   [[5, ['A042']], [3, ['A025', 'B004']]])

a1 = ['A043', 'B004', 'A025', 'A042', 'C025']
a2 = ['B009', 'B040', 'B003', 'A042', 'A027', 'A044']
a3 = ['A041', 'A026', 'B005']
test.assert_equals(id_best_users(a1, a2, a3), [])

a1 = ['A042', 'B004', 'A025', 'A042', 'C025']
a2 = ['B009', 'B040', 'B004', 'A042', 'A025', 'A042']
a3 = ['A042', 'B004', 'A025', 'A042', 'C025', 'B009', 'B040', 'B004', 'A042',
      'A025', 'A042']
a4 = ['A042', 'A025', 'B004']
test.assert_equals(id_best_users(a1, a2, a3, a4),
                   [[9, ['A042']], [5, ['A025', 'B004']]])
