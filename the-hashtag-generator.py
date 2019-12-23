# https://www.codewars.com/kata/the-hashtag-generator/train/python
from test import Test


def generate_hashtag(s):
    words = s.split()
    result = f'#{"".join([word.capitalize() for word in words])}'
    if 1 < len(result) <= 140:
        return result
    else:
        return False


Test.describe("Basic tests")
Test.assert_equals(generate_hashtag(''), False, 'Expected an empty string to return False')
Test.assert_equals(generate_hashtag('Do We have A Hashtag')[0], '#', 'Expeted a Hashtag (#) at the beginning.')
Test.assert_equals(generate_hashtag('Codewars'), '#Codewars', 'Should handle a single word.')
Test.assert_equals(generate_hashtag('Codewars      '), '#Codewars', 'Should handle trailing whitespace.')
Test.assert_equals(generate_hashtag('Codewars Is Nice'), '#CodewarsIsNice', 'Should remove spaces.')
Test.assert_equals(generate_hashtag('codewars is nice'), '#CodewarsIsNice',
                   'Should capitalize first letters of words.')
Test.assert_equals(generate_hashtag('CodeWars is nice'), '#CodewarsIsNice',
                   'Should capitalize all letters of words - all lower case but the first.')
Test.assert_equals(generate_hashtag('c i n'), '#CIN',
                   'Should capitalize first letters of words even when single letters.')
Test.assert_equals(generate_hashtag('codewars  is  nice'), '#CodewarsIsNice',
                   'Should deal with unnecessary middle spaces.')
Test.assert_equals(generate_hashtag(
    'Looooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooong Cat'),
    False, 'Should return False if the final word is longer than 140 chars.')
