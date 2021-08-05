from typing import Counter
from scripts.Task1 import countTextUsers

texts1 = [[1, 1, 'bla'], [1, 1, 'bla']]
texts2 = [[1, 1, 'bla'], [2, 1, 'bla']]
texts3 = [[1, 3, 'bla'], [2, 1, 'bla'], [1, 3, 'bla']]
texts4 = [[1, 3, 'bla'], [2, 1, 'bla'], [2, 1, 'bla'], [1, 3, 'bla']]


def test_countTextusers_returns_3():
    assert countTextUsers(texts3) == 3
