from datetime import datetime
from dateutil.relativedelta import relativedelta

"""
This program calculates a person's exact age based on the input date of birth and prints the age in various formats including:
- Years, months, and days
- Total months and days
- Total weeks and days
- Total days
- Total hours
- Total minutes
- Total seconds

The program also calculates how many days are remaining until the next birthday or anniversary.

Steps:
1. The user provides their birth year, month, and day.
2. The program calculates the difference between the current date and the birth date using the `relativedelta` module.
3. It then prints the user's age in different time units.
4. Finally, it computes how many days are left until the next birthday or anniversary.
"""

def ageCalculator(y, m, d):
    now = datetime.now()
    dob = datetime(y, m, d)
    
    delta = relativedelta(now, dob)

    years = delta.years
    months = delta.months
    days = delta.days

    print(f"Your current age is {years} years, {months} months, and {days} days.")

    total_days = (now - dob).days
    total_months = years * 12 + months
    total_weeks = total_days // 7
    remaining_days_weeks = total_days % 7
    total_hours = total_days * 24 + now.hour
    total_minutes = total_hours * 60 + now.minute
    total_seconds = total_minutes * 60 + now.second

    print(f"Or {total_months} months and {days} days.")
    print(f"Or {total_weeks} weeks and {remaining_days_weeks} days.")
    print(f"Or {total_days} days.")
    print(f"Or {total_hours} hours.")
    print(f"Or {total_minutes} minutes.")
    print(f"Or {total_seconds} seconds.")

    # Calculate the remaining days until the next birthday
    next_birthday = datetime(now.year, m, d)
    if now > next_birthday:
        next_birthday = datetime(now.year + 1, m, d)
    
    remaining_days = (next_birthday - now).days
    print(f"Your next birthday/anniversary is in {remaining_days} days.")

year = int(input("Enter year of birth: "))
month = int(input("Enter month of birth: "))
date = int(input("Enter date of birth: "))

ageCalculator(year, month, date)
