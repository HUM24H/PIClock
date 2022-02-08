import datetime
import subprocess
import sys

class Reset:
    def __init__(self, rtc):
        self.rtc = rtc
        
    def Initialise(self):
        self.rtc.set_battery_switchover('level_switching_mode')

        h = int(subprocess.check_output("date '+%H'", shell=True))
        m = int(subprocess.check_output("date '+%M'", shell=True))
        s = int(subprocess.check_output("date '+%S'", shell=True))
        Y = int(subprocess.check_output("date '+%Y'", shell=True))
        M = int(subprocess.check_output("date '+%m'", shell=True))
        D = int(subprocess.check_output("date '+%d'", shell=True))

        t = datetime.time(h, m, s)
        d = datetime.date(Y, M, D)

        self.rtc.set_time(t)
        self.rtc.set_date(d)