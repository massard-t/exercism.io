class Clock(object):

    def __init__(self, hours, minutes):
        self.hours = hours
        self.minutes = minutes
        self.hours = (self.hours + (self.minutes // 60)) % 24
        self.minutes = self.minutes % 60

    def __str__(self):
        self.hours = (self.hours + (self.minutes // 60)) % 24
        self.minutes = self.minutes % 60
        return "{0:02d}:{1:02d}".format(self.hours, self.minutes)

    def __eq__(self, arg):
        return self.hours == arg.hours and self.minutes == arg.minutes

    def __nq__(self, arg):
        return self.hours != arg.hours or self.minutes != arg.minutes

    def add(self, arg):
        return Clock(self.hours, self.minutes + arg)
