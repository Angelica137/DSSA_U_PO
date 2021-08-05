from scripts.Task1 import countTextUsers

import csv
with open('scripts/texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

texts1 = [[1, 1, 'bla'], [1, 1, 'bla']]


def test_countTextUsers_retutns_texts():
    assert countTextUsers(texts1) == [1]
