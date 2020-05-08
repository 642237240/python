class Time(object):
    def print_time(self):
        print('%.2d:%.2d:%.2d' % (self.hour, self.minute, self.second))

    def time_to_int(self):
        return self.hour*3600+self.minute*60+self.second

    def is_after(self, other):
        return self.time_to_int() > other.time_to_int()

    def __init__(self, hour=0, minute=0, second=0):
        self.hour = hour
        self.minute = minute
        self.second = second

    def __str__(self):
        return '%.2d:%.2d:%.2d' % (self.hour, self.minute, self.second)

    def int_to_time(self, second):
        self.hour = second // 3600
        self.minute = (second % 3600) // 60
        self.second = second % 60
        return self


start = Time()
start.hour = 9
start.minute = 45
start.second = 0
Time.print_time(start)
start.print_time()
print(start.time_to_int())
# print(start.time_to_int())
print(start.int_to_time(start.time_to_int()))
time = Time(9)
time.print_time()
print(time)
time = Time(9,45)
print(time)
time.print_time()
time = Time()
print(time)
time.print_time()
