# make a  task in taskschd.msc  so every xx min the script will be run
import ctypes 
user32 = ctypes.windll.LoadLibrary('user32.dll')
import time, datetime
import win32api  
WM_APPCOMMAND = 0x319
APPCOMMAND_VOLUME_MAX = 0x0a
APPCOMMAND_VOLUME_MIN = 0x09


today = datetime.datetime.fromtimestamp(time.time()) ## get time
hour = int(today.strftime("%H")) ##get hour
if (hour>=0) and (hour<=15):
    #LOCK screen during night
    user32.LockWorkStation()
    #MUTE
    win32api.SendMessage(-1, WM_APPCOMMAND, 0x30292, APPCOMMAND_VOLUME_MIN * 0x10000)
