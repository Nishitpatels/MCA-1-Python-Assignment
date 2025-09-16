from datetime import date 

birth = date(2004, 9, 20)
today = date.today()

years = today.year - birth.year
month = today.month - birth.month
day = today.day - birth.day

# Adjust for negatives
if day < 0:
    month -= 1
    day += 30
if month < 0:
    years -= 1
    month += 12

print(f"I am {years} Years, {month} Months & {day} Days old.")