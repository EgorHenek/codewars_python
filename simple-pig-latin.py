# https://www.codewars.com/kata/520b9d2ad5c005041100000f/train/python
from test import Test


def pig_it(text: str):
    result = []
    words = text.split()
    for word in words:
        if word.isalpha():
            result.append(f'{word[1:]}{word[0]}ay')
        else:
            result.append(word)
    return ' '.join(result)


Test.assert_equals(pig_it('Pig latin is cool'), 'igPay atinlay siay oolcay')
Test.assert_equals(pig_it('This is my string'), 'hisTay siay ymay tringsay')
Test.assert_equals(pig_it('Hello world !'), 'elloHay orldway !')
