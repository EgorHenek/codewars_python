# https://www.codewars.com/kata/55ddb0ea5a133623b6000043/train/python
import re

from test import Test as test


def class_name_changer(cls, new_name):
    if re.match(r'^[A-Z][\w]+$', new_name):
        cls.__name__ = new_name
    else:
        raise


class MyClass:
    pass


myObject = MyClass()
test.assert_equals(MyClass.__name__, "MyClass")

class_name_changer(MyClass, "UsefulClass")
test.assert_equals(MyClass.__name__, "UsefulClass")

class_name_changer(MyClass, "SecondUsefulClass")
test.assert_equals(MyClass.__name__, "SecondUsefulClass")
