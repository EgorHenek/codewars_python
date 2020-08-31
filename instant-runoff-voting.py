# https://www.codewars.com/kata/52996b5c99fdcb5f20000004/train/python
from typing import Optional
from collections import Counter

from test import Test


def runoff(votes: list) -> Optional[str]:
    while votes[0]:
        result = Counter([vote[0] for vote in votes])
        winner, max_score = max(result.items(), key=lambda x: x[1])
        min_score = min(result.values())
        if max_score * 2 > len(votes):
            return winner
        votes = [[c for c in vote if result[c] > min_score] for vote in votes]


voters = [["dem", "ind", "rep"],
          ["rep", "ind", "dem"],
          ["ind", "dem", "rep"],
          ["ind", "rep", "dem"]]

Test.assert_equals(runoff(voters), "ind")

voters = [["a", "c", "d", "e", "b"],
          ["e", "b", "d", "c", "a"],
          ["d", "e", "c", "a", "b"],
          ["c", "e", "d", "b", "a"],
          ["b", "e", "a", "c", "d"]]
Test.assert_equals(runoff(voters), None)
