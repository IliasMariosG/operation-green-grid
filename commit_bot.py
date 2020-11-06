import os
import datetime
import time

timestamp = datetime.datetime.now()
os.system("echo '%s' >> time_date_log.txt" % timestamp)
# time.sleep(1)
os.system("git add .")
# time.sleep(1)
os.system("git commit -m 'Add new timestamp to time_date_log'")
# time.sleep(1)
os.system("git push")


