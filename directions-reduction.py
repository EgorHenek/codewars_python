# https://www.codewars.com/kata/550f22f4d758534c1100025a/train/python
from test import Test


def dirReduc(arr):
    compass = ['NORTH', 'EAST', 'SOUTH', 'WEST']
    stack = []
    for direction in arr:
        reversed_direction = compass[compass.index(direction) - 2]
        if stack and stack[-1] == reversed_direction:
            stack.pop(-1)
        else:
            stack.append(direction)
    return stack


a = ["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]
Test.assert_equals(dirReduc(a), ['WEST'])
u = ["NORTH", "WEST", "SOUTH", "EAST"]
Test.assert_equals(dirReduc(u), ["NORTH", "WEST", "SOUTH", "EAST"])
