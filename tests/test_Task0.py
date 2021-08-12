from scripts.Task0 import first_text, last_call

import csv
with open('scripts/texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)


with open('scripts/calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


def test_first_text_returns_first_text():
    assert first_text(
        texts) == "First record of texts, 97424 22395 texts 90365 06212 at time 01-09-2016 06:03:22"


def test_last_call_returns_last_call():
    assert last_call(
        calls) == "Last record of calls, 98447 62998 calls (080)46304537 at time 30-09-2016 23:57:15, lasting 2151 seconds"
