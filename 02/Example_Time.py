class Time:
    """Represents the time of day.
       
    attributes: hour, minute, second
    """

    def __init__(self, hour=0, minute=0, second=0):
        """Initializes a time object.
        hour: int
        minute: int
        second: int or float
        """
        self.hour = hour
        self.minute = minute
        self.second = second

    def __str__(self):
        """Returns a string representation of the time."""
        return '%.2d:%.2d:%.2d' % (self.hour, self.minute, self.second)

    def print_time(self):
        """Prints a string representation of the time."""
        print(str(self)) 

    def __add__(self, other):
        """Adds two Time objects or a Time object and a number.
        other: Time object or number of seconds
        """
        if isinstance(other, Time):
            return self._add_time(other)
        else:
            return self.increment(other)

    def __radd__(self, other):
        """Adds two Time objects or a Time object and a number."""
        return self.__add__(other)

    def is_after(self, other):
        """Returns True if t1 is after t2; false otherwise."""
        return self._time_to_int() > other._time_to_int()

    def _add_time(self, other):
        """Adds two time objects."""
        assert self._is_valid() and other._is_valid()
        seconds = self._time_to_int() + other._time_to_int()
        return self._int_to_time(seconds)

    def increment(self, seconds):
        """Returns a new Time that is the sum of this time and seconds."""
        seconds += self._time_to_int()
        return self._int_to_time(seconds)

    def _time_to_int(self):
        """Computes the number of seconds since midnight."""
        minutes = self.hour * 60 + self.minute
        seconds = minutes * 60 + self.second
        return seconds

    def _int_to_time(self, seconds):
        """Makes a new Time object.
        seconds: int seconds since midnight.
        """
        minutes, second = divmod(seconds, 60)
        hour, minute = divmod(minutes, 60)
        time = Time(hour, minute, second)
        return time

    def _is_valid(self):
        """Checks whether a Time object satisfies the invariants."""
        if self.hour < 0 or self.minute < 0 or self.second < 0:
            return False
        if self.minute >= 60 or self.second >= 60:
            return False
        return True


def main():
    start = Time(9, 45, 00)    # calling __init__()
    start.print_time            

    end = start.increment(1337)
    end.print_time()

    print('Is end after start?')
    print(end.is_after(start))

    print('Using __str__')
    print(start, end)         # calling __str__()

    start = Time(9, 45)
    duration = Time(1, 35)    
    print(start + duration)   # calling __add__()
    print(start + 1337)       # calling __add__()
    print(1337 + start)       # calling __radd__()

    # Example of polymorphism
    t1 = Time(7, 43)
    t2 = Time(7, 41)
    t3 = Time(7, 37)
    total = sum([t1, t2, t3])
    print(total)


if __name__ == '__main__':
    main()