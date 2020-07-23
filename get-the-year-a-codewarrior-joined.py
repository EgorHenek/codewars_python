# https://www.codewars.com/kata/58ab2ed1acbab2eacc00010e/train/python
import re
from urllib.request import urlopen

from bs4 import BeautifulSoup

from test import Test


def get_member_since(username: str) -> str:
    response = urlopen(f'https://www.codewars.com/users/{username}')
    soup = BeautifulSoup(response.read(), 'html.parser')
    since = soup.select_one(
        'div.flex-box > div:nth-of-type(2) > div:nth-of-type(1)').text
    since = re.findall(r':([\w\s]+)$', since)
    return since[0]


Test.assert_equals(get_member_since('jhoffner'), 'Oct 2012')
