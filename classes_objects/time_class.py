class Time:
    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def printTime(self):
        print str(self.hours) + ":" + str(self.minutes) + ":" + str(self.seconds)
