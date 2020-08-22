# https://www.codewars.com/kata/55ddcef532f8678af1000006/train/python
import re

from test import Test as test


class ReNameAbleClass:
    @classmethod
    def change_class_name(cls, new_name):
        if re.match(r'^[A-Z][\w]+$', new_name):
            cls.__name__ = new_name
        else:
            raise

    @classmethod
    def __str__(cls):
        return f'Class name is: {cls.__name__}'


class MyClass(ReNameAbleClass):
    pass


myObject = MyClass()
test.assert_equals(
    str(myObject),
    "Class name is: MyClass",
    "Original class name shouldn't be changed yet...",
)

myObject.change_class_name("UsefulClass")
test.assert_equals(
    str(myObject),
    "Class name is: UsefulClass",
    "New class name should be as boss wanted to!",
)

myObject.change_class_name("SecondUsefulClass")
test.assert_equals(
    str(myObject),
    "Class name is: SecondUsefulClass",
    "New class name should be as boss wanted to!",
)
