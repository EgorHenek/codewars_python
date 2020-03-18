# https://www.codewars.com/kata/51f2b4448cadf20ed0000386/train/python
from test import Test


def remove_url_anchor(url):
    pos = url.find('#')
    if pos > 0:
        return url[:pos]
    else:
        return url


Test.assert_equals(remove_url_anchor("www.codewars.com#about"), "www.codewars.com");
Test.assert_equals(remove_url_anchor("www.codewars.com/katas/?page=1#about"), "www.codewars.com/katas/?page=1")
Test.assert_equals(remove_url_anchor("www.codewars.com/katas/"), "www.codewars.com/katas/")
