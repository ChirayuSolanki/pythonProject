# datetime,time,calender
#time→ Epoch method → when time start's→using of local time function → struct_time → ctime() function
#datetime→now()→today's()
from datetime import *
dt = datetime.now()
print(dt)
print("Current Time : ",dt.strftime("%H:%M:%S"))

