import os
import datetime
import time
import random

start_time = datetime.datetime.now()
while 1:
  timestamp = datetime.datetime.now()
  os.system("echo '%s' >> time_date_log.txt" % timestamp)
  os.system("git add .")
  os.system("git commit -m 'Add new timestamp to time_date_log'")
  os.system("git push")
  time.sleep(random.randint(0, 60))


