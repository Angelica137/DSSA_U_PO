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


def isTelemarketer(calls, texts):
    telemarketers = []
    not_telemarketers = []
    for call in calls:
        if call[0] not in telemarketers or call[0] not in not_telemarketers:
            not_in_texts = True
            for text in texts:
                if call[0] in text:
                    not_in_texts = False
                    not_telemarketers.append(call[0])
            if not_in_texts == True:
                telemarketers.append(call[0])
    return telemarketers


def noIncomingCalls(calls):
    telemarketers = []
    not_telemarketers = []
    for call in calls:
        incoming_calls = False
        for i in range(len(calls)):
            if call[0] == calls[i][1]:
                print(call[0])
                print(calls[i][1])
                incoming_calls = True
                not_telemarketers.append(call[0])
                print("these are not telemarketers " +
                      str(not_telemarketers))
                i += 1
        if incoming_calls == False:
            telemarketers.append(call[0])

    return telemarketers


calls2 = [['1408371123', '98453 94494', '01-09-2016 06:01:12', '186'],
          ['1408371456', '(022)28952819', '01-09-2016 06:01:59', '2093'],
          ['97424 22395', '93427 40118', '01-09-2016 06:03:51', '1975'],
          ['93427 40118', '97424 22395', '01-09-2016 06:11:23', '1156'],
          ['(080)67362492', '90356 11723', '01-09-2016 07:24:45', '2258'],
          ['90356 11723', '(080)67362492', '01-09-2016 07:24:45', '2258']]

calls = [['1408371942', '98453 94494', '01-09-2016 06:01:12', '186'],
         ['1408371333', '(022)28952819', '01-09-2016 06:01:59', '2093'],
         ['97424 22395', '(022)47410783', '01-09-2016 06:03:51', '1975'],
         ['93427 40118', '(080)33118033', '01-09-2016 06:11:23', '1156'],
         ['(080)67362492', '(04344)316423', '01-09-2016 07:24:45', '2258']]


texts = [['97424 22395', '97416 29480', '14-09-2016 20:52:17'],
         ['93427 40118', '93422 47940', '14-09-2016 20:58:50'],
         ['90356 11723', '81525 12041', '14-09-2016 20:59:30'],
         ['90366 36573', '97425 12708', '14-09-2016 21:00:07'],
         ['97424 53609', '97385 70012', '14-09-2016 21:01:01'],
         ['93410 56456', '98453 86521', '14-09-2016 21:03:52']]


print(isTelemarketer(calls, texts))
print(noIncomingCalls(calls2))
