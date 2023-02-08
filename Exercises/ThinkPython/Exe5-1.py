import time

secs = time.time()

def time():
  mins = secs / 60
  hours = mins / 60
  days = hours/24
  print('Minutes:',mins,'\nHours:' ,hours, '\nDays:',days)

time()
print('Seconds:', secs)
print()
print()

import time
epoch=time.time()

#60*60*24=86400
total_sec = epoch % 86400
#60*60
hours = int(total_sec/3600)
total_minutes = int(total_sec/60)
mins = total_minutes % 60
sec = int(total_sec % 60)

days=int(epoch/86400)

print("The Current time is",hours,':',mins,':',sec)
print("Days since epoch:", days)
