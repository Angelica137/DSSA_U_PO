from scripts.Task0 import firstText

import csv
with open('scripts/texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)


def test_firstText_returns_first_text():
    assert firstText(
        texts) == "First record of texts, 97424 22395 texts 90365 06212 at time 01-09-2016 06:03:22"
