from scripts.Task2 import longestCall

calls = [['78130 00821', '98453 94494', '01-09-2016 06:01:12', '186'], ['78298 91466',
                                                                        '(022)28952819', '01-09-2016 06:01:59', '2093'], ['97424 22395', '(022)47410783', '01-09-2016 06:03:51', '1975']]


def test_longestCall_returns_10():
    assert longestCall(calls) == 2093
