# make a  task in taskschd.msc  so every xx min the script will be run
import time, datetime
import subprocess



today = datetime.datetime.fromtimestamp(time.time()) ## get time
hour = int(today.strftime("%H")) ##get hour
if (hour>=0) and (hour<=19):
    #Hibernate
    subprocess.Popen("rundll32 powrprof.dll,SetSuspendState Hibernate")

