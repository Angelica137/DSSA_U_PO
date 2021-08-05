from typing import Counter
from scripts.Task1 import countUniquetNumbers

texts1 = [[1, 1, 'bla'], [1, 1, 'bla']]
texts2 = [[1, 1, 'bla'], [2, 1, 'bla']]
texts3 = [[1, 3, 'bla'], [2, 1, 'bla'], [1, 3, 'bla']]
texts4 = [[1, 3, 'bla'], [2, 1, 'bla'], [2, 1, 'bla'], [1, 3, 'bla']]

calls = [[1, 3, 'bla', 'bla'], [2, 5, 'bla', 'bla'],
         [2, 1, 'bla', 'bla'], [1, 3, 'bla', 'bla']]


def test_countUniqueNumbers_returns_3():
    assert countUniquetNumbers(texts3, calls) == 4
