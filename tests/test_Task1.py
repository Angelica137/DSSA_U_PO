from typing import Counter
from scripts.Task1 import countTextUsers

texts1 = [[1, 1, 'bla'], [1, 1, 'bla']]
texts2 = [[1, 1, 'bla'], [2, 1, 'bla']]


def test_countTextUsers_retutns_1():
    assert countTextUsers(texts1) == [1]


def test_countTextUsers_returns_1_and_2():
    assert countTextUsers(texts2) == [1, 2]
