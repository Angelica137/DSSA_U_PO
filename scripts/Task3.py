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
    area_codes = []
    for call in calls:
        if '(080)' in call[0]:
            if call[1][0:3] == '140' and '140' not in area_codes:
                area_codes.append('140')
            if ')' in call[1] and call[1][0:call[1].find(')') + 1] not in area_codes:
                area_codes.append(call[1][0:call[1].find(')') + 1])
            if ' ' in call[1] and call[1][0:call[1].find(' ')] not in area_codes:
                area_codes.append(call[1][0:call[1].find(' ')])
    area_codes_ordered = sorted(area_codes)
    return area_codes_ordered


'''
Big Oh Calculation receivingAreaCodesBangalore(calls):

area_codes = [] -> 1 step
for call in calls: -> n steps
    if '(080)' in call[0]: -> O(n)
        if call[1][0:3] == '140' and '140' not in area_codes: -> O(k) + 1 + O(n)
            area_codes.append('140') -> 1 step
        if ')' in call[1] and call[1][0:call[1].find(')') + 1] not in area_codes: -> O(k) + O(k)
            area_codes.append(call[1][0:call[1].find(')') + 1]) -> 1 step
        if ' ' in call[1] and call[1][0:call[1].find(' ')] not in area_codes: -> O(k) + O(k)
            area_codes.append(call[1][0:call[1].find(' ')]) -> 1 step
area_codes_ordered = sorted(area_codes) -> O(nlogn)
return area_codes_ordered -> 1 step

Big O = O(n)
'''


def callsToBangalore(calls):
    calls_from_bangalore = 0
    count = 0
    for call in calls:
        if '(080)' in call[0]:
            calls_from_bangalore += 1
            if '(080)' in call[1]:
                count += 1
    percentage = round((count / calls_from_bangalore * 100), 2)
    return percentage


'''
Big Oh Calculation callsToBangalore(calls):

calls_from_bangalore = 0 -> 1 step
count = 0 -> 1 step
for call in calls: -> n steps
    if '(080)' in call[0]: -> n steps
        calls_from_bangalore += 1 -> 1 step
        if '(080)' in call[1]: -> k steps
            count += 1 -> 1 step
percentage = round((count / calls_from_bangalore * 100), 2) -> 1 step (docs say todo)
return percentage -> 1 step

Big O = O(n)
'''


'''
Answer Part A
'''
codes = receivingAreaCodesBangalore(calls)
copyA = "The numbers called by people in Bangalore have codes:"
print(copyA)
for elem in codes:
    print(elem)


'''
Answer part B
'''
percentage_bangalore = callsToBangalore(calls)
copyB = " percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore."
print(str(percentage_bangalore) + copyB)
