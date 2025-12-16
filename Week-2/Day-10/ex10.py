# Print current time only

import datetime as dt
import time

current_time=dt.datetime.now().strftime("%H:%M:%S")

c_time=time.strftime("%H:%M:%S")

print("The current time is :",current_time)
print("The current time is :",c_time)