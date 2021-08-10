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
TASK 0:
What is the first record of texts and what is the last record of calls?
Print messages:
"First record of texts, <incoming number> texts <answering number> at time <time>"
"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
"""

# Print the first record of texts


def firstText(texts):
    '''
    Returns the first record of texts
    '''
    incoming = texts[0][0]
    answering = texts[0][1]
    time = texts[0][2]
    result = "First record of texts, {} texts {} at time {}".format(
        incoming, answering, time)
    return result


'''
Big Oh Calculation firstText(texts):

incoming = texts[0][0] -> 1 step
answering = texts[0][1] -> 1 step
time = texts[0][2] -> 1 step
result = ... -> 1 step
return result -> 1 step

Big O = O(1)
'''


def lastCall(calls):
    '''
    Print the alst record of calls
    '''
    incomingNo = calls[-1][0]
    receiving = calls[-1][1]
    time = calls[-1][2]
    duration = calls[-1][3]
    resultCall = "Last record of calls, " + incomingNo + " calls " + \
        receiving + " at time " + time + ", lasting " + duration + " seconds"
    return resultCall


'''
Big Oh Calculation lastCall(calls):

incomingNo = calls[-1][0] -> 1 step
receiving = calls[-1][1] -> 1 step
time = calls[-1][2] -> 1 step
duration = calls[-1][3] - 1 step
resultCall = ... -> 1 step
return resultCall -> 1 step

Big O = O(1)
'''


'''
Print statements Task0
'''

print(firstText(texts))
print(lastCall(calls))
