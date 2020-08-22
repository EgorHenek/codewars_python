# https://www.codewars.com/kata/55dec8f72ead8624e5000028/train/python

from test import Test as test


def create_class(class_name, secrets=None):
    if class_name:
        return type(class_name, (), secrets or {})


def army_get_secret_from_file():
    return {
        'secret_func1': lambda self: 'This is secret function, test #01',
        'secret_func2': lambda self, x: f'This is secret function with value'
                                        f' = {x}, test #02',
        'prop1': 12.345,
        'prop2': 'some test values'
    }


armyClass = create_class('new one', army_get_secret_from_file())
army_object = armyClass()
test.assert_equals(army_object.secret_func1(),
                   "This is secret function, test #01",
                   "Should return from secret function #01")
test.assert_equals(army_object.secret_func2(44),
                   "This is secret function with value = 44, test #02",
                   "Should return from secret function #02")
test.assert_equals(army_object.prop1, 12.345, "Should return secret property")
test.assert_equals(army_object.prop2, "some test values",
                   "Should return secret property")
