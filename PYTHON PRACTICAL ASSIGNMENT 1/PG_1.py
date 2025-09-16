from datetime import date 

# Input two dates in YYYY-MM-DD format

d1 = date(2025, 9, 20)
d2 = date(2026, 9, 20)

# Difference
diff = d2 - d1
print("Difference in Days: ",diff.days)