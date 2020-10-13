#!usr/bin/python3
# A function to add time.

# The function should add the duration time to the start time and return the
#  result.
# If the result will be the next day, it should show (next day) after the time.
# If the result will be more than one day later, it should show (n days later)
#  after the time, where "n" is the number of days later.
# If the function is given the optional starting day of the week parameter,
#  then the output should display the day of the week of the result. The day of
#  the week in the output should appear after the time and before the number of
#  days later.

def add_time(start_time, added_time, day=''):
    """Takes a start time and adds the indicated amount of time."""
    # Parse the start time and added time.
    start_time_digits, am_or_pm = start_time.split()
    start_time_hrs, start_time_mins = start_time_digits.split(':')
    added_time_hrs, added_time_mins = added_time.split(':')
    
    # Add the time together.
    total_hrs = int(start_time_hrs) + int(added_time_hrs)
    total_mins = int(start_time_mins) + int(added_time_mins)

    # Simplify down to 12-hour time.
    new_hour = (total_hrs % 12) + (total_mins // 60)
    new_min = total_mins % 60
    if len(str(new_min)) == 1:
        new_min = f"0{new_min}"
    new_time = f"{new_hour}:{new_min} "

    # Determine AM PM switch, if any. 1 = switch 0 = no switch.
    if new_hour == 12:
        total_hrs += 1
    
    am_pm_switch = (total_hrs // 12) % 2
    if am_pm_switch == 0:
        new_time = new_time + am_or_pm
    elif am_pm_switch == 1:
        if am_or_pm == 'AM':
            new_time = new_time + 'PM'
        else:
            new_time = new_time + 'AM'
    # If the new hour is 12, it needs to change AM/PM...

    # Determine number of days passed, if any.
    if am_or_pm == 'PM':
        days_passed = ((total_hrs // 12) + 1) // 2
    else:
        days_passed = (total_hrs // 12) // 2

    # Determine new day of the week, if provided and changed.
    if day:
        day = day.lower()
        current_day = None
                
        if day == 'monday':
            current_day = 1
        elif day == 'tuesday':
            current_day = 2
        elif day == 'wednesday':
            current_day = 3
        elif day == 'tthursday':
            current_day = 4
        elif day == 'friday':
            current_day = 5
        elif day == 'saturday':
            current_day = 6
        elif day == 'sunday':
            current_day = 7

        new_day = (current_day + days_passed) % 7

        days_of_week = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday',
            'Friday', 'Saturday']
        
        # Compile new day into new time.
        new_time = new_time + f", {days_of_week[new_day]}"

    
    # Compile days passed into new time.
    if days_passed == 1:
        new_time = new_time + " (next day)"
    elif days_passed > 1:
        new_time = new_time + f" ({days_passed} days later)"

    print(new_time)

add_time("10:00 PM", "1:05")
add_time("10:45 AM", "3:30")
add_time("10:45 PM", "13:30", "tuesday")
add_time("10:45 PM", "3413:30", "friday")