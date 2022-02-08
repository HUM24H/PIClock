# PIClock
Welcome to my Raspberry Pi Clock project

The hardware used in this project is below:
- Raspberry Pi 4
- RV3028 RTC I2C Module
- LED DOT Matrix 5x7 (2xRED + 1xGREEN)
- Breakout Garden for Raspberry Pi

Notes:
- LED DOT Matrix Displays
	- Two of these will need to be physically modified to have different I2C addresses.
	- The default I2C address is 0x61. You can change this to 0x63 by cutting the trace on the back of the breakout. If you cut the trace and solder the bridge the address will be 0x62 - so it's possible to use up to three of these breakouts at the same time
- RV3028
	- I found frequent access to the I2C caused delays, this is why the code resets to RTC module every 24 hours to keep it in sync
- Always online
	- I keep my clock connected to the Internet but the beauty of the RTC is you can run it completely offline
	- Be warned that the RV3028 is very accurate but like all RTC's they do drift over time
