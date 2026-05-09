'''Write a program that:

Gets today's date

Checks:

if last_completed_date is None

Prints:

"First time task completed"'''

from datetime import date

today = date.today()

print(today)

last_completed_date = None

if last_completed_date is None:
    print("First time task completed")
else:
    print("This is not first ")

    