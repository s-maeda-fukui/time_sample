import datetime
import time

if __name__ == "__main__":
    time_stop = datetime.datetime.today()
    min_stop = time_stop.minute+1

    while True:
       time_stamp = datetime.datetime.today()
       print(time_stamp.hour,end=":")
       print(time_stamp.minute,end=":")
       print(time_stamp.second)

       if min_stop == time_stamp.minute:
               break

       time.sleep(5)
