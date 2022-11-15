#!/usr/bin/env python
import schedule
import time
from message import message

def main():
    message()

if __name__ == '__main__':
    schedule.every().day.at("07:00").do(main)

    while True:

        # Checks whether a scheduled task
        # is pending to run or not
        schedule.run_pending()
        # Sleep for 1 hour
        time.sleep(60)
