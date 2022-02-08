class LEDTime:
    def __init__(self, displ, dispm, dispr, rtc):
        self.displ = displ
        self.dispm = dispm
        self.dispr = dispr
        self.rtc = rtc

    def LEDClockTime(self, time):
        hour_one = int(str(time)[0])
        hour_two = int(str(time)[1])

        minute_one = int(str(time)[3])
        minute_two = int(str(time)[4])

        second_one = int(str(time)[6])
        second_two = int(str(time)[7])

        self.displ.set_character(0, str(hour_one))
        self.displ.set_character(5, str(hour_two))
        self.displ.set_brightness(0.1)
        self.displ.show()

        self.dispm.set_character(0, str(second_one))
        self.dispm.set_character(5, str(second_two))
        self.dispm.set_brightness(0.1)
        self.dispm.show()

        self.dispr.set_character(0, str(minute_one))
        self.dispr.set_character(5, str(minute_two))
        self.dispr.set_brightness(0.1)
        self.dispr.show()

    #Get time from RTC
    def RTCGetTime(self):
        time = self.rtc.get_time()

        return time

    #Routine to clear and show each display
    def LEDClear(self):
        self.displ.clear()
        self.displ.show()

        self.dispm.clear()
        self.dispm.show()

        self.dispr.clear()
        self.dispr.show()