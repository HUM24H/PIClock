#!/usr/bin/python3
from smbus import SMBus #SMBUS I2C library
from ltp305 import LTP305 #LED Matrix I2C library 
from rv3028 import RV3028 #RTC I2C library
from ControllerLED import LEDTime #Import LED Controller Script
from ControllerReset import Reset #Import Reset Controller Script
from datetime import datetime, timedelta #Import date/time functions

#Setup the 3 displays and set correct addresses for each
display_left = LTP305(address=0x61)
display_middle = LTP305(address=0x62)
display_right = LTP305(address=0x63)

#Setup RTC and set correct address
rtc = RV3028(i2c_addr=0x52)

#Main controller routine
def Controller():
    #Setup LED Controller & Reset Controller Classes
    LED = LEDTime(display_left, display_middle, display_right, rtc)
    RES = Reset(rtc)

    #On first run reset RTC
    RES.Initialise()

    #On first run clear the LED displays
    LED.LEDClear()

    #On first run grab current date/time
    reset_datetime = datetime.now().replace(microsecond=0) + timedelta(hours=24)

    #Indefinite loop to keep updating the LED displays with the time
    while True:
        if (datetime.now().replace(microsecond=0) == reset_datetime):
            #24 hours have passed so reset RTC
            RES.Initialise()
            #Reset our variable with next 24 hour reset date/time
            reset_datetime = datetime.now().replace(microsecond=0) + timedelta(hours=24)

        #Get RTC time
        time = LED.RTCGetTime()

        #Set LED time
        LED.LEDClockTime(time)

#Call the controller
Controller()