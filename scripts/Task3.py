"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('scripts/texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('scripts/calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore. In other words, the calls were initiated by "(080)" area code
to the following area codes and mobile prefixes:
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""


def receivingAreaCodesBangalore(calls):
    unique_area_codes = []
    for call in calls:
        if '(080)' in call[0]:
            if call[1][0:3] == '140' and '140' not in unique_area_codes:
                unique_area_codes.append('140')
            if ')' in call[1] and call[1][0:call[1].find(')') + 1] not in unique_area_codes:
                unique_area_codes.append(call[1][0:call[1].find(')') + 1])
            if ' ' in call[1] and call[1][0:call[1].find(' ')] not in unique_area_codes:
                unique_area_codes.append(call[1][0:call[1].find(' ')])

    return unique_area_codes


def fixedLinesUnique(calls):
    codes = fixedLines(calls)
    unique_codes = []
    for code in codes:
        if code not in unique_codes:
            unique_codes.append(code)
    return unique_codes


def mobileCodes(calls):
    recepients = callFromBangalore(calls)
    mobile_area_codes = []
    for number in recepients:
        if ' ' in number:
            code = number[0:number.find(' ')]
            if code not in mobile_area_codes:
                mobile_area_codes.append(number[0:number.find(' ')])
    return mobile_area_codes


calls2 = [['(080)33118033', '98453 94494', '01-09-2016 06:01:12', '186'],
          ['(080)33118033', '(022)28952819', '01-09-2016 06:01:59', '2093'],
          ['97424 22395', '(022)47410783', '01-09-2016 06:03:51', '1975'],
          ['93427 40118', '(080)33118033', '01-09-2016 06:11:23', '1156'],
          ['(080)67362492', '(04344)316423', '01-09-2016 07:24:45', '2258'],
          ['(080)67362492', '1408371942', '01-09-2016 07:24:45', '2258'],
          ['(080)33118033', '(022)28952819', '01-09-2016 06:01:59', '2093']]


print(receivingAreaCodesBangalore(calls2))
