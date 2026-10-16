from datetime import date , time , datetime

today = date.today()
now = datetime.now()
print("Today's data is", today)
print("Current Date and time is ", now)

print("Date components", today.year, today.month, today.day)