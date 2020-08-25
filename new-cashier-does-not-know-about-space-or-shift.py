# https://www.codewars.com/kata/5d23d89906f92a00267bb83d
from test import Test


def get_order(order):
    menu = {
        'Burger': 0,
        'Fries': 0,
        'Chicken': 0,
        'Pizza': 0,
        'Sandwich': 0,
        'Onionrings': 0,
        'Milkshake': 0,
        'Coke': 0,
    }

    for item in menu:
        menu[item] = order.count(item.lower())
    return ''.join(
        [f'{item} ' * count for item, count in menu.items()]
    ).strip()


Test.assert_equals(
    get_order(
        "milkshakepizzachickenfriescokeburgerpizzasandwichmilkshakepizza"
    ),
    "Burger Fries Chicken Pizza Pizza Pizza Sandwich Milkshake Milkshake Coke"
)
Test.assert_equals(
    get_order("pizzachickenfriesburgercokemilkshakefriessandwich"),
    "Burger Fries Fries Chicken Pizza Sandwich Milkshake Coke"
)
