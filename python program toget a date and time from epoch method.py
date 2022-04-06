# converting the epoch time into date and time
import time
epoch= time.time()
print(epoch)
t = time.localtime(epoch)

#retrive the date from the structure t
d = t.tm_mday
m = t.tm_mon
y = t.tm_year
print("Current Date is : %d - %d -%d"%(d,m,y))

#retrive the time from from structure t
h = t.tm_hour
n = t.tm_min
s = t.tm_sec
print('Current time: %d :%d :%d' % (h,n,s))


