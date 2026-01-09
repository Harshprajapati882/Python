# Python `datetime` Module

The `datetime` module in Python provides classes for working with dates and times. It is a powerful tool for manipulating and formatting dates and times.

## Getting the Current Date and Time

You can get the current date and time using the `datetime.now()` method.

```python
import datetime

# Get the current date and time
now = datetime.datetime.now()
print(f"Current date and time: {now}")

# Get the current date
today = datetime.date.today()
print(f"Current date: {today}")
```

## Creating Specific Date and Time Objects

You can create a `datetime` object for a specific date and time.

```python
import datetime

# Create a specific date
d = datetime.date(2023, 10, 26)
print(f"Specific date: {d}")

# Create a specific time
t = datetime.time(10, 30, 0)
print(f"Specific time: {t}")

# Create a specific datetime
dt = datetime.datetime(2023, 10, 26, 10, 30, 0)
print(f"Specific datetime: {dt}")
```

## Formatting and Parsing Dates

You can format dates as strings and parse strings into `datetime` objects.

### Formatting Dates (`strftime`)

The `strftime()` method formats a `datetime` object into a string.

```python
import datetime

now = datetime.datetime.now()

# Format the date and time
formatted_date = now.strftime("%Y-%m-%d %H:%M:%S")
print(f"Formatted date: {formatted_date}")

# More formatting options
print(f"Year: {now.strftime('%Y')}")
print(f"Month: {now.strftime('%B')}")
print(f"Day: {now.strftime('%d')}")
print(f"Weekday: {now.strftime('%A')}")
```

### Parsing Dates (`strptime`)

The `strptime()` method parses a string into a `datetime` object.

```python
import datetime

date_string = "2023-10-26 10:30:00"

# Parse the string into a datetime object
parsed_date = datetime.datetime.strptime(date_string, "%Y-%m-%d %H:%M:%S")
print(f"Parsed date: {parsed_date}")
```

## Date Arithmetic

You can perform arithmetic operations on `datetime` objects.

```python
import datetime

now = datetime.datetime.now()

# Add 10 days to the current date
ten_days_from_now = now + datetime.timedelta(days=10)
print(f"10 days from now: {ten_days_from_now}")

# Subtract 2 weeks from the current date
two_weeks_ago = now - datetime.timedelta(weeks=2)
print(f"2 weeks ago: {two_weeks_ago}")

# Calculate the difference between two dates
date1 = datetime.datetime(2023, 10, 26)
date2 = datetime.datetime(2023, 11, 15)
difference = date2 - date1
print(f"Difference between dates: {difference.days} days")
```

## Timezones

The `datetime` module can also handle timezones. You need to use a library like `pytz` for full timezone support.

First, install `pytz`:
```bash
pip install pytz
```

Then, you can work with timezones:

```python
import datetime
import pytz

# Get the current time in a specific timezone
ny_timezone = pytz.timezone("America/New_York")
ny_time = datetime.datetime.now(ny_timezone)
print(f"New York time: {ny_time.strftime('%Y-%m-%d %H:%M:%S %Z%z')}")

# Convert a naive datetime to an aware datetime
naive_dt = datetime.datetime.now()
aware_dt = ny_timezone.localize(naive_dt)
print(f"Aware datetime in New York: {aware_dt.strftime('%Y-%m-%d %H:%M:%S %Z%z')}")
```
