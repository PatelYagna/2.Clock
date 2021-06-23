#module for controling time related programs.
import time

#setting the standard time.
seconds = 0
minutes = 0
hours = 0

#Forever loop.
while True:
    #prints the hours then minutes and then seconds. Each seprated with a colon.
    print(str(hours).zfill(2) + ":" + str(minutes).zfill(2) + ":" + str(seconds).zfill(2))
    #Increases second by 1
    seconds = seconds + 1
    #it mimics the time in real time. So every second 'the second' changes.
    time.sleep(1)
    #Statements for changeing the minute, and hours on the correct time.
    if seconds == 60:
        seconds = 0
        minutes = minutes + 1
    if minutes == 60:
        minutes = 0
        hours = hours + 1