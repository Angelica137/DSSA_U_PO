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


def countTextUsers(texts):
    unique_numbers = []
    for text in texts:
        if text not in unique_numbers:
            unique_numbers.append(text)
    return unique_numbers
