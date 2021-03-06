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


def calls_from_bangalore(calls):
    area_codes = []  # O(1)
    for call in calls:  # O(n)
        if '(080)' in call[0]:  # O(nm)
            if call[1][0:3] == '140':  # O(nm)
                area_codes.append('140')  # O(1)
            if ')' in call[1]:  # O(nm)
                # O(1) + O(k) + O(nm) + O(1)
                area_codes.append(call[1][0:call[1].find(')') + 1])
            if ' ' in call[1]:  # O(nm)
                area_codes.append(call[1][0:4])  # O(1)
    unique_codes = set(area_codes)  # O(1)
    sort_codes = sorted(unique_codes)  # O(n log n)
    bangalore_pc = round(
        (area_codes.count('(080)')/len(area_codes) * 100), 2)  # O(1)
    return sort_codes, bangalore_pc  # O(1)


answers = calls_from_bangalore(calls)

'''
Answer Part A
'''

copy_a = "The numbers called by people in Bangalore have codes:"
print(copy_a)
for elem in answers[0]:
    print(elem)


'''
Answer part B
'''

print("{} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.".format(
    answers[1]))
