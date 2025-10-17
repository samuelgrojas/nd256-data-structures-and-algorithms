"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
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

outgoing_calls = set()
incoming_calls = set()
text_senders = set()
text_receivers = set()

for record in calls:
    outgoing_calls.add(record[0])
    incoming_calls.add(record[1])

for record in texts:
    text_senders.add(record[0])
    text_receivers.add(record[1])

possible_telemarketers = outgoing_calls - incoming_calls - text_senders - text_receivers
print("These numbers could be telemarketers: ")
for number in sorted(possible_telemarketers):
    print(number)

