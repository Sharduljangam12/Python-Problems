from datetime import date,timedelta

today = date.today()

print(today)
print(today + timedelta(days=1))

last_completed_date = None
streak = 0

if streak == 1:
    print("Already completed today")
elif streak <= 0:
    print("Streak incremented")
elif streak >= 1:
    print("Streak Broken")