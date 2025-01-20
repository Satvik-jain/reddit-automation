import schedule
import time
from reddit_instance import posting

TIME = "21:41" 
# Set the time accordingly
# Script can be automated using Task Scheduler in windows

schedule.every().day.at(TIME).do(posting)

while True:
    schedule.run_pending()
    time.sleep(1)