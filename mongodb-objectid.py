# https://www.codewars.com/kata/52fefe6cb0091856db00030e/train/python
from test import Test

from datetime import datetime
import re


class Mongo(object):

    @classmethod
    def is_valid(cls, s):
        return isinstance(s, str) and bool(re.match(r'[0-9a-f]{24}$', s))

    @classmethod
    def get_timestamp(cls, s):
        return cls.is_valid(s) and datetime.fromtimestamp(int(s[:8], 16))


Test.assert_equals(Mongo.is_valid(False), False)
Test.assert_equals(Mongo.is_valid([]), False)
Test.assert_equals(Mongo.is_valid(1234), False)
Test.assert_equals(Mongo.is_valid('123476sd'), False)
Test.assert_equals(Mongo.is_valid('507f1f77bcf86cd79943901'), False)
Test.assert_equals(Mongo.is_valid('507f1f77bcf86cd799439016'), True)

Test.assert_equals(Mongo.get_timestamp(False), False)
Test.assert_equals(Mongo.get_timestamp([]), False)
Test.assert_equals(Mongo.get_timestamp(1234), False)
Test.assert_equals(Mongo.get_timestamp('123476sd'), False)
Test.assert_equals(Mongo.get_timestamp('507f1f77bcf86cd79943901'), False)
Test.assert_equals(Mongo.get_timestamp('507f1f77bcf86cd799439016'), datetime(2012, 10, 17, 21, 13, 27))
