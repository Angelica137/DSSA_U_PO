from scripts.Task1 import unique_numbers

texts = [[1, 3, 'bla'], [2, 1, 'bla'], [2, 1, 'bla'], [1, 3, 'bla']]

calls = [[1, 3, 'bla', 'bla'], [2, 5, 'bla', 'bla'],
         [2, 1, 'bla', 'bla'], [1, 3, 'bla', 'bla']]

calls2 = [[1, 3, 'bla', 'bla'], [2, 5, 'bla', 'bla'],
          [2, 1, 'bla', 'bla'], [1, 3, 'bla', 'bla'], [4, 3, 'bla', 'bla']]


def test_unique_numbers_returns_4():
    assert unique_numbers(
        texts, calls) == "There are 4 different telephone numbers in the records."


def test_unique_numbers_returns_5():
    assert unique_numbers(
        texts, calls2) == "There are 5 different telephone numbers in the records."
