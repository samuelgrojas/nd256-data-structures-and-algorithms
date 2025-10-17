"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
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

time_on_phone = {}
for record in calls:
    calling_number = record[0]
    receiving_number = record[1]
    duration = int(record[3])
    
    if calling_number in time_on_phone:
        time_on_phone[calling_number] += duration
    else:
        time_on_phone[calling_number] = duration
    
    if receiving_number in time_on_phone:
        time_on_phone[receiving_number] += duration
    else:
        time_on_phone[receiving_number] = duration

print(f"{max(time_on_phone, key=time_on_phone.get)} spent the longest time, {time_on_phone[max(time_on_phone, key=time_on_phone.get)]} seconds, on the phone during September 2016.")

