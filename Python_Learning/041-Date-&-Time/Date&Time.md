# Python Date and Time

Python provides several modules for working with dates and times. The most important ones are `time`, `datetime`, and `calendar`.

---

## `time` module

The `time` module provides various time-related functions.

### `time.time()`
Returns the current time as a floating-point number, representing seconds since the epoch (January 1, 1970).

```python
import time

seconds_since_epoch = time.time()
print(f"Seconds since epoch: {seconds_since_epoch}")
```

### `time.ctime()`
Returns a string representing the current local time.

```python
import time

current_local_time = time.ctime()
print(f"Current local time: {current_local_time}")
```

### `time.sleep()`
Suspends execution for a specified number of seconds.

```python
import time

print("Sleeping for 2 seconds...")
time.sleep(2)
print("Woke up!")
```

### `time.localtime()` and `time.struct_time` (TimeTuple)
`time.localtime()` returns a `time.struct_time` object (also known as a TimeTuple) with local time components.

```python
import time

local_time_tuple = time.localtime()
print(f"Local time tuple: {local_time_tuple}")
print(f"Year: {local_time_tuple.tm_year}")
print(f"Month: {local_time_tuple.tm_mon}")
print(f"Day: {local_time_tuple.tm_mday}")
```

### `time.asctime()`
Accepts a `time.struct_time` object or a tuple of 9 integers and returns a 24-character string representing it.

```python
import time

local_time_tuple = time.localtime()
print(f"Formatted time string: {time.asctime(local_time_tuple)}")
```

### `time.altzone`
The offset of the local DST timezone, in seconds west of UTC, if one is defined.

```python
import time

print(f"Timezone offset in seconds: {time.altzone}")
```

### `time.clock()` (Deprecated)
`time.clock()` is deprecated since Python 3.3 and was removed in Python 3.8. Use `time.perf_counter()` or `time.process_time()` instead.

- `time.perf_counter()`: Returns the value (in fractional seconds) of a performance counter, i.e. a clock with the highest available resolution to measure a short duration.
- `time.process_time()`: Returns the value (in fractional seconds) of the sum of the system and user CPU time of the current process.

```python
import time

start_perf = time.perf_counter()
start_process = time.process_time()

# Perform some work
for i in range(1000000):
    pass

end_perf = time.perf_counter()
end_process = time.process_time()

print(f"Performance counter elapsed time: {end_perf - start_perf} seconds")
print(f"Process time elapsed: {end_process - start_process} seconds")
```

---

## `datetime` module

The `datetime` module supplies classes for working with dates and times.

### `datetime.datetime.now()`
Returns the current date and time.

```python
import datetime

now = datetime.datetime.now()
print(f"Current date and time: {now}")
```

### `date` objects
For working with dates only.
```python
import datetime

today = datetime.date.today()
print(f"Today's date: {today}")
```

### Instance Methods of `datetime` objects

Here are some useful instance methods for `datetime` objects.

#### `replace()`
Returns a new `datetime` object with some attributes replaced.
```python
import datetime

dt = datetime.datetime(2023, 10, 26, 10, 30, 0)
new_dt = dt.replace(year=2024, month=11)
print(f"Original datetime: {dt}")
print(f"Replaced datetime: {new_dt}")
```

#### `timetuple()`
Returns a `time.struct_time` object.
```python
import datetime

now = datetime.datetime.now()
time_tuple = now.timetuple()
print(f"Time tuple from datetime: {time_tuple}")
```

#### `toordinal()`
Returns the proleptic Gregorian ordinal of the date, where January 1 of year 1 has ordinal 1.
```python
import datetime

now = datetime.datetime.now()
ordinal_date = now.toordinal()
print(f"Ordinal date: {ordinal_date}")
```

#### `weekday()` and `isoweekday()`
- `weekday()`: Returns the day of the week as an integer (Monday is 0 and Sunday is 6).
- `isoweekday()`: Returns the day of the week as an integer (Monday is 1 and Sunday is 7).
```python
import datetime

now = datetime.datetime.now()
print(f"Weekday (0-6): {now.weekday()}")
print(f"ISO Weekday (1-7): {now.isoweekday()}")
```

#### `isoformat()`
Returns a string representing the date and time in ISO 8601 format.
```python
import datetime

now = datetime.datetime.now()
iso_date = now.isoformat()
print(f"ISO format date: {iso_date}")
```

#### `__str__()`
Returns a string representation of the `datetime` object.
```python
import datetime

now = datetime.datetime.now()
print(f"String representation: {str(now)}")
```

---

## `calendar` module

The `calendar` module provides functions related to the calendar.

### `calendar.month()`
Prints a calendar for a specific month.

```python
import calendar

yy = 2023
mm = 10
print("\nCalendar for October 2023:")
print(calendar.month(yy, mm))
```

### `calendar.calendar()`
Prints a calendar for the entire year.

```python
import calendar

# print("\nCalendar for the year 2024:")
# print(calendar.calendar(2024))
```

### `calendar.isleap()`
Checks if a year is a leap year.

```python
import calendar

print(f"Is 2024 a leap year? {calendar.isleap(2024)}")
```

### More `calendar` functions

#### `calendar.weekday()`
Returns the day of the week (0 is Monday) for `year`, `month`, `day`.
```python
import calendar

print(f"Weekday for 2023-10-26: {calendar.weekday(2023, 10, 26)}")
```

#### `calendar.monthrange()`
Returns a tuple containing the weekday of the first day of the month and the number of days in the month.
```python
import calendar

print(f"Month range for Oct 2023: {calendar.monthrange(2023, 10)}")
```