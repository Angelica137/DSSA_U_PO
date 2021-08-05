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
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""


def uniquetNumbers(texts, calls):
    records = texts + calls
    unique_numbers = []
    for record in records:
        if record[0] not in unique_numbers:
            unique_numbers.append(record[0])
        if record[1] not in unique_numbers:
            unique_numbers.append(record[1])
    count_unique_nos = len(unique_numbers)
    return count_unique_nos
