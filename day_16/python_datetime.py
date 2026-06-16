# Day 16 - Python Date and Time
# Python has a built-in module called datetime.
# It helps us work with dates, times, current date, formatting, and differences.


# 1. Import datetime module
import datetime


# 2. Get current date and time
current_datetime = datetime.datetime.now()

print("Current date and time:", current_datetime)
print("Current year:", current_datetime.year)
print("Current month:", current_datetime.month)
print("Current day:", current_datetime.day)
print("Current hour:", current_datetime.hour)
print("Current minute:", current_datetime.minute)
print("Current second:", current_datetime.second)


# 3. Get only today's date
today = datetime.date.today()

print("Today's date:", today)
print("Year:", today.year)
print("Month:", today.month)
print("Day:", today.day)


# 4. Create custom date
birth_date = datetime.date(2002, 5, 15)

print("Birth date:", birth_date)


# 5. Create custom time
office_start_time = datetime.time(9, 30, 0)

print("Office start time:", office_start_time)
print("Office hour:", office_start_time.hour)
print("Office minute:", office_start_time.minute)


# 6. Create custom date and time together
meeting_datetime = datetime.datetime(2026, 6, 16, 10, 30, 0)

print("Meeting date and time:", meeting_datetime)


# 7. Format date using strftime()
# strftime() converts date/time into a readable string format.
formatted_date = current_datetime.strftime("%d-%m-%Y")
formatted_time = current_datetime.strftime("%I:%M %p")
formatted_full = current_datetime.strftime("%A, %d %B %Y")

print("Formatted date:", formatted_date)
print("Formatted time:", formatted_time)
print("Formatted full date:", formatted_full)


# 8. Common strftime format codes
# %Y = full year, like 2026
# %y = short year, like 26
# %m = month number, like 06
# %B = full month name, like June
# %b = short month name, like Jun
# %d = day number, like 16
# %A = full weekday name, like Tuesday
# %a = short weekday name, like Tue
# %H = hour in 24-hour format
# %I = hour in 12-hour format
# %M = minute
# %S = second
# %p = AM or PM


# 9. Convert string to date using strptime()
# strptime() converts a string into a datetime object.
date_string = "16-06-2026"
converted_date = datetime.datetime.strptime(date_string, "%d-%m-%Y")

print("Converted date:", converted_date)
print("Converted date year:", converted_date.year)


# 10. Date difference
# We can subtract two dates to get the difference.
start_date = datetime.date(2026, 6, 1)
end_date = datetime.date(2026, 6, 16)

difference = end_date - start_date

print("Date difference:", difference)
print("Difference in days:", difference.days)


# 11. Real-world example: calculate age
birth_date = datetime.date(2002, 5, 15)
today = datetime.date.today()

age = today.year - birth_date.year

if (today.month, today.day) < (birth_date.month, birth_date.day):
    age = age - 1

print("Age:", age)


# 12. timedelta
# timedelta is used to add or subtract days, hours, minutes, etc.
today = datetime.date.today()
tomorrow = today + datetime.timedelta(days=1)
yesterday = today - datetime.timedelta(days=1)
next_week = today + datetime.timedelta(days=7)

print("Today:", today)
print("Tomorrow:", tomorrow)
print("Yesterday:", yesterday)
print("Next week:", next_week)


# 13. Real-world example: subscription expiry
subscription_start = datetime.date(2026, 6, 1)
subscription_days = 30
subscription_end = subscription_start + datetime.timedelta(days=subscription_days)

print("Subscription start:", subscription_start)
print("Subscription end:", subscription_end)

if today <= subscription_end:
    print("Subscription is active")
else:
    print("Subscription expired")


# 14. Real-world example: delivery date
order_date = datetime.date.today()
delivery_after_days = 5
delivery_date = order_date + datetime.timedelta(days=delivery_after_days)

print("Order date:", order_date)
print("Expected delivery date:", delivery_date)


# 15. Real-world example: task deadline check
deadline = datetime.date(2026, 6, 30)
today = datetime.date.today()

days_left = deadline - today

if days_left.days > 0:
    print("Days left for deadline:", days_left.days)
elif days_left.days == 0:
    print("Deadline is today")
else:
    print("Deadline passed by", abs(days_left.days), "days")


# 16. Real-world example: attendance login time
login_time = datetime.datetime(2026, 6, 16, 9, 45, 0)
office_time = datetime.datetime(2026, 6, 16, 9, 30, 0)

late_by = login_time - office_time

if login_time > office_time:
    print("Employee is late by:", late_by)
else:
    print("Employee is on time")


# 17. Real-world example: generate invoice number using date
current_datetime = datetime.datetime.now()
invoice_number = current_datetime.strftime("INV-%Y%m%d-%H%M%S")

print("Invoice number:", invoice_number)


# 18. Real-world example: log message with timestamp
log_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
log_message = "[" + log_time + "] User logged in"

print("Log message:", log_message)


# 19. Import specific classes from datetime
from datetime import date, time, timedelta

custom_date = date(2026, 12, 25)
custom_time = time(18, 0, 0)
after_three_days = date.today() + timedelta(days=3)

print("Custom date:", custom_date)
print("Custom time:", custom_time)
print("After three days:", after_three_days)


# 20. What should you know about datetime?
# - datetime.datetime.now() gives current date and time
# - datetime.date.today() gives only today's date
# - date(year, month, day) creates a custom date
# - time(hour, minute, second) creates a custom time
# - strftime() converts date/time to string
# - strptime() converts string to date/time
# - timedelta is used to add or subtract time
# - You can subtract dates to find the difference
# - Date and time are used in invoices, logs, expiry, attendance, booking, and reports
