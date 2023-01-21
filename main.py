import argparse
import time
parser=argparse.ArgumentParser()
import os
import datetime

parser.add_argument("time",help="Enter time in Hours,Mins and seconds")


args=parser.parse_args()
x=args.time
try:
    hours=int(x.split("h")[0])
except ValueError:
    hours=0
except IndexError:
    hours=0
try:
    mins=int(x.split("h")[1].split("m")[0])
except ValueError:
    mins=0
except IndexError:
    try:
        mins=int(x.split("m")[0])
    except IndexError:
        mins=0
    except ValueError:
        mins=0
try:
    secs=int(x.split("h")[1].split("m")[1].split("s")[0])
except ValueError:
    secs=0
except IndexError:
    try:
        secs=int(x.split("m")[1].split("s")[0])
    except IndexError:
        secs=int(x.split("s")[0])
seconds=(hours*60*60)+(mins*60)+secs

for i in range(seconds,-1,-1):
    convert = str(datetime.timedelta(seconds = i))
    time.sleep(1)
    print(f"Time remaining: {convert}",end="\r")
    #time.sleep(0.5)
    #os.system("cls")
print("Timer Ended")