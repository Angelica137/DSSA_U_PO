from scripts.Task3 import callFromBangalore, telemarkerterCodes, fixedLines, fixedLinesUnique, mobileCodes, areaCodes

calls = [['78130 00821', '98453 94494', '01-09-2016 06:01:12', '186'],
         ['78298 91466', '(022)28952819', '01-09-2016 06:01:59', '2093'],
         ['97424 22395', '(022)47410783', '01-09-2016 06:03:51', '1975'],
         ['93427 40118', '(080)33118033', '01-09-2016 06:11:23', '1156']]


calls1 = [['(080)33118033', '98453 94494', '01-09-2016 06:01:12', '186'],
          ['78298 91466', '(022)28952819', '01-09-2016 06:01:59', '2093'],
          ['97424 22395', '(022)47410783', '01-09-2016 06:03:51', '1975'],
          ['93427 40118', '(080)33118033', '01-09-2016 06:11:23', '1156']]


calls2 = [['(080)33118033', '98453 94494', '01-09-2016 06:01:12', '186'],
          ['(080)33118033', '(022)28952819', '01-09-2016 06:01:59', '2093'],
          ['97424 22395', '(022)47410783', '01-09-2016 06:03:51', '1975'],
          ['93427 40118', '(080)33118033', '01-09-2016 06:11:23', '1156'],
          ['(080)67362492', '(04344)316423', '01-09-2016 07:24:45', '2258'],
          ['(080)67362492', '1408371942', '01-09-2016 07:24:45', '2258'],
          ['(080)33118033', '(022)28952819', '01-09-2016 06:01:59', '2093']]


def test_callFromBanaglore_returns_empty():
    assert callFromBangalore(calls) == []


def test_callFromBanaglore_returns_calls1():
    assert callFromBangalore(calls1) == ['98453 94494']


def test_callFromBanaglore_returns_calls2():
    assert callFromBangalore(calls2) == [
        '98453 94494', '(022)28952819', '(04344)316423', '1408371942', '(022)28952819']


def test_telemarketersCodes_returns_1408371942():
    assert telemarkerterCodes(calls2) == ['140']


def test_fixedLines_return_area_codes():
    assert fixedLines(calls2) == ['(022)', '(04344)', '(022)']


def test_fixedLinesSimple_return_unique_area_codes():
    assert fixedLinesUnique(calls2) == ['(022)', '(04344)']


def test_callFromBanaglore_returns_calls2():
    assert mobileCodes(calls2) == ['98453']


def test_areaCodes_returns_area_codes():
    assert mobileCodes(calls2) == ['98453', '(022)', '(04344)', '140']
