import time
import datetime
import calendar

# time module
seconds_since_epoch = time.time()
print(f"Seconds since epoch: {seconds_since_epoch}")

current_local_time = time.ctime()
print(f"Current local time: {current_local_time}")

print("Sleeping for 2 seconds...")
time.sleep(2)
print("Woke up!")

local_time_tuple = time.localtime()
print(f"Local time tuple: {local_time_tuple}")
print(f"Year: {local_time_tuple.tm_year}")
print(f"Month: {local_time_tuple.tm_mon}")
print(f"Day: {local_time_tuple.tm_mday}")

print(f"Formatted time string: {time.asctime(local_time_tuple)}")
print(f"Timezone offset in seconds: {time.altzone}")

start_perf = time.perf_counter()
start_process = time.process_time()

# Perform some work
for i in range(1000000):
    pass

end_perf = time.perf_counter()
end_process = time.process_time()

print(f"Performance counter elapsed time: {end_perf - start_perf} seconds")
print(f"Process time elapsed: {end_process - start_process} seconds")


# datetime module
now = datetime.datetime.now()
print(f"Current date and time: {now}")

today = datetime.date.today()
print(f"Today's date: {today}")

dt = datetime.datetime(2023, 10, 26, 10, 30, 0)
new_dt = dt.replace(year=2024, month=11)
print(f"Original datetime: {dt}")
print(f"Replaced datetime: {new_dt}")

time_tuple = now.timetuple()
print(f"Time tuple from datetime: {time_tuple}")

ordinal_date = now.toordinal()
print(f"Ordinal date: {ordinal_date}")

print(f"Weekday (0-6): {now.weekday()}")
print(f"ISO Weekday (1-7): {now.isoweekday()}")

iso_date = now.isoformat()
print(f"ISO format date: {iso_date}")

print(f"String representation: {str(now)}")


# calendar module
yy = 2023
mm = 10
print("\nCalendar for October 2023:")
print(calendar.month(yy, mm))

# print("\nCalendar for the year 2024:")
# print(calendar.calendar(2024))

print(f"Is 2024 a leap year? {calendar.isleap(2024)}")

print(f"Weekday for 2023-10-26: {calendar.weekday(2023, 10, 26)}")

print(f"Month range for Oct 2023: {calendar.monthrange(2023, 10)}")

# New functions to get day, date, time and calendar

def get_current_day():
    """Returns the current day of the week as a string."""
    now = datetime.datetime.now()
    return now.strftime("%A")

def get_current_date():
    """Returns the current date as a formatted string."""
    today = datetime.date.today()
    return today.strftime("%B %d, %Y")

def get_current_time():
    """Returns the current time as a formatted string."""
    now = datetime.datetime.now()
    return now.strftime("%H:%M:%S")

def display_current_month_calendar():
    """Displays the calendar for the current month."""
    now = datetime.datetime.now()
    yy = now.year
    mm = now.month
    print(f"\nCalendar for {now.strftime('%B %Y')}:")
    print(calendar.month(yy, mm))

# Example usage of the new functions
print(f"\nCurrent day: {get_current_day()}")
print(f"Current date: {get_current_date()}")
print(f"Current time: {get_current_time()}")
display_current_month_calendar()