def day_finder(day,day_add):
    week = ['MONDAY','TUESDAY','WEDNESDAY','THURSDAY','FRIDAY','SATURDAY','SUNDAY']
    pos = week.index(day)
    for c in range(day_add):
        pos += 1
        if pos == 7:
            pos = 0
    return week[pos]

def add_time(start, duration, day=None):

    # Defining starting info     
    items = start.split()
    time = items[0]
    if day != None:
        day = day.upper().strip()

    # Creating variables     
    pos = time.find(':')
    hours = int(time[:pos])
    minutes = int(time[pos+1:])
    am_or_pm = items[1]

    pos = duration.find(':')
    hours_add = int(duration[:pos])
    minutes_add = int(duration[pos+1:])
    day_add = 0

    # Adding the minutes
    for c in range(minutes_add):

        minutes += 1

        if  minutes == 60:
            minutes = 0
            hours_add += 1

    # Adding the hours
    for c in range(hours_add):
        hours += 1
        if hours == 12:
            hours = 0
            if am_or_pm == 'PM':
                day_add += 1
            if am_or_pm == 'AM':
                am_or_pm = 'PM'
            elif am_or_pm == 'PM':
                am_or_pm = 'AM'     

    # Tweaking some info
    if len(str(minutes)) == 1:
        minutes = '0' + str(minutes)
    if hours == 0:
        hours = 12
    
    # Defining the result
    time_result = str(hours) + ':' + str(minutes) + ' ' + am_or_pm

    # If day was given add day to the result
    if day != None:
        time_result += f', {day_finder(day,day_add).capitalize()}'

    # If at least one day has passed add it to the result
    if day_add >= 1:
        if day_add == 1:
            time_result += ' (next day)'
        else:
            time_result += f' ({day_add} days later)'


    return time_result