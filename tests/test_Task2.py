import csv
from scripts.Task2 import longestCall

calls1 = [['78130 00821', '98453 94494', '01-09-2016 06:01:12', '186'], ['78298 91466',
                                                                         '(022)28952819', '01-09-2016 06:01:59', '2093'], ['97424 22395', '(022)47410783', '01-09-2016 06:03:51', '1975']]


calls2 = [['78130 00821', '98453 94494', '01-09-2016 06:01:12', '50000'], ['78298 91466',
                                                                           '(022)28952819', '01-09-2016 06:01:59', '2093'], ['97424 22395', '(022)47410783', '01-09-2016 06:03:51', '1975']]

with open('scripts/calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

'''
def test_longestCall_returns_calls1():
    assert longestCall(calls1) == '78298 91466'


def test_longestCall_returns_calls2():
    assert longestCall(calls2) == '78130 00821'


def test_longestCall_returns_10():
    assert longestCall(calls) == '89071 50880'
'''
