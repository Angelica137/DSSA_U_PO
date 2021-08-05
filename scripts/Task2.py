"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('scripts/texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('scripts/calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""


def longestCall(calls):
    longest_call = 0
    for call in calls:
        minutes = int(call[3])
        if minutes > longest_call:
            longest_call = minutes
    return longest_call


print(longestCall(calls))
