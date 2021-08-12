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


def longest_call(calls):
    '''
    returns the number that spent the longest time on the phone this period
    '''
    call_times = {}  # O(1)
    count = 0
    for call in calls:  # O(n)
        if call[0] in call_times:  # O(n)
            call_times[call[0]] += int(call[3])  # 1 step + O(n)
            # print('a')
            count += 1
        if call[1] in call_times:  # O(n)
            call_times[call[1]] += int(call[3])  # 1 step + O(n)
            # print('b')
            count += 1
        else:
            if call[0] not in call_times:  # O(n)
                call_times[call[0]] = int(call[3])  # 1 step + O(n)
                # print('c')
                count += 1
            if call[1] not in call_times:
                call_times[call[1]] = int(call[3])  # 1 step + O(n)
                # print('d')
                count += 1
        #print("round " + str(count))
        # print(call_times)

    max_time = max(call_times.values())  # O(n)
    number = [k for k, v in call_times.items() if v == max_time][0]  # O(n) + 1
    copy = "{} spent the longest time, {} seconds, on the phone during September 2016."  # 1 step
    answer_task2 = copy.format(number, max_time)  # 1 step + O(n)?
    return answer_task2  # 1 step


print(longest_call(calls))


calls4 = [['78130 00821', '98453 94494', '01-09-2016 06:01:12', '500'],
          ['78298 91466', '(022)28952819', '01-09-2016 06:01:59', '2093'],
          ['(022)47410783', '98453 94494', '01-09-2016 06:01:12', '3000'],
          ['97424 22395', '(022)47410783', '01-09-2016 06:03:51', '1975'],
          ['97424 22395', '(022)47410783', '01-09-2016 06:03:51', '1975'],
          ['(080)33251027', '98453 94494', '01-09-2016 06:01:12', '5000']]


print(longest_call(calls4))
