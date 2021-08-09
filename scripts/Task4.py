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
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""


def notInTexts(calls, texts):
    '''
    returns the numbers that do not send or
    receive texts
    '''
    no_texts = []
    for call in calls:
        if call[0] not in no_texts:
            not_in_texts = True
            for text in texts:
                if call[0] in text:
                    not_in_texts = False
            if not_in_texts == True:
                no_texts.append(call[0])
    return no_texts


'''
Big Oh Calculation notInTexts(calls, texts):

no_texts = [] -> 1 step
for call in calls: -> n steps
    if call[0] not in no_texts: -> n steps
        not_in_texts = True = 1 step
        for text in texts: -> n steps
            if call[0] in text: -> n steps
                not_in_texts = False -> 1 step
        if not_in_texts == True: -> 1 step
            no_texts.append(call[0]) -> 1 step
return no_texts

Big O = O(n^2)
'''


def noIncomingCalls(numbers, calls):
    '''
    returns the numbers that do not receive any calls
    '''
    no_incoming_calls = []
    for number in numbers:
        incoming_calls = False
        for i in range(len(calls)):
            if number == calls[i][1]:
                incoming_calls = True
                i += 1
        if incoming_calls == False and number not in no_incoming_calls:
            no_incoming_calls.append(number)
    return no_incoming_calls


'''
Big Oh Calculation noIncomingCalls(numbers, calls):

no_incoming_calls = [] -> 1 step
for number in numbers: -> n steps
    incoming_calls = False -> 1 step
    for i in range(len(calls)): -> n steps
        if number == calls[i][1]: -> 1 step
            incoming_calls = True -> 1 step
            i += 1 -> 1 step
    if incoming_calls == False and number not in no_incoming_calls: -> 1 step + k steps
        no_incoming_calls.append(number) -> 1 step
return no_incoming_calls -> step

Big O = O(n^2)
'''


def findTelemarketers(calls, texts):
    no_texts = notInTexts(calls, texts)  # O(n^2)
    telemarketers = noIncomingCalls(no_texts, calls)  # O(n^2)
    ordered_numbers = sorted(telemarketers)  # O(nlogn)
    return ordered_numbers


'''
Answer
'''
possible_telemarketers = findTelemarketers(calls, texts)
copy = "These numbers could be telemarketers: "
print(copy)
for elem in possible_telemarketers:
    print(elem)
