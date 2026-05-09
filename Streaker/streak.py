from datetime import date, timedelta #in this step i have imported date class from datetime module 

today = date.today() 
''''today = date.today()
→ Calls a class method (today()) of the date class
→ It returns the current system date (YYYY-MM-DD)
→ That value is stored in the variable today'''
print(today) # this is the link that used to print the value of variable

print(today + timedelta(days=1)) 

last_completed_date = None
streak = 0