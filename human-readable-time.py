# https://www.codewars.com/kata/52685f7382004e774f0001f7/train/python
from test import Test


def make_readable(seconds):
    h = seconds // 3600
    m = (seconds % 3600) // 60
    s = (seconds % 3600) % 60

    return '{:02d}:{:02d}:{:02d}'.format(h, m, s)


Test.assert_equals(make_readable(0), "00:00:00")
Test.assert_equals(make_readable(5), "00:00:05")
Test.assert_equals(make_readable(60), "00:01:00")
Test.assert_equals(make_readable(86399), "23:59:59")
Test.assert_equals(make_readable(359999), "99:59:59")
