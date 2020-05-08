class Time(object):
    """Represents the time of day.

    attributes: hour, minute, second
    """


time = Time()
time.hour = 11
time.minute = 59
time.second = 30


def format_time(t):
    return '%.2d:%.2d:%.2d' % (t.hour, t.minute, t.second)


def print_time(t):
    print(format_time(t))


print_time(time)


def is_after(t1, t2):
    if t1.hour > t2.hour:
        return True
    if t1.hour == t2.hour and t1.minute > t2.minute:
        return True
    if t1.hour == t2.hour and t1.minute == t2.minute and t1.second > t2.second:
        return True
    else:
        return False


def is_after1(t1, t2):
    return t1.hour*3600+t1.minute*60+t1.second > t2.hour*3600+t2.minute*60+t2.second


t1 = Time()
t2 = Time()
t1.hour = 11
t1.minute = 59
t1.second = 29
print('%s is after %s? %d' % (format_time(time), format_time(t1), is_after1(time, t1)))
t1.hour = 11
t1.minute = 58
t1.second = 31
print('%s is after %s? %d' % (format_time(time), format_time(t1), is_after1(time, t1)))
t1.hour = 12
t1.minute = 58
t1.second = 31
print('%s is after %s? %d' % (format_time(time), format_time(t1), is_after1(time, t1)))


def add_time(t1, t2):
    sum = Time()
    sum.hour = t1.hour + t2.hour
    sum.minute = t1.minute + t2.minute
    sum.second = t1.second + t2.second

    if sum.second >= 60:
        sum.second -= sum.second
        sum.minute += 1
    if sum.minute >= 60:
        sum.minute -= sum.minute
        sum.hour += 1
    return sum


start = Time()
start.hour = 9
start.minute = 45
start.second = 0

duration = Time()
duration.hour = 1
duration.minute = 35
duration.second = 0

done = add_time(start, duration)
print_time(done)
