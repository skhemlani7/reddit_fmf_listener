import generate
import time
import win10toast
from sys import platform
import os

#TODO: Run on startup
#   https://www.quora.com/How-do-I-run-a-Python-script-on-a-startup-on-Windows

#   https://stackoverflow.com/questions/8220108/how-do-i-check-the-operating-system-in-python
#   https://stackoverflow.com/questions/58161208/how-do-i-send-a-notification-with-python-to-mac-notifications-center
#   https://stackoverflow.com/questions/17651017/python-post-osx-notification

def sendNotification(platform, title, text):
    if platform[:3] == 'win':
        toaster = win10toast.ToastNotifier()
        toaster.show_toast(title, text, duration=15)
    elif platform == 'darwin':
        os.system("""
                osascript -e 'display notification "{}" with title "{}"'
                """.format(text, title))
    else:
        pass
    return

my_list = []
my_list.append(generate.parse_reddit())
while True:
    temp = generate.parse_reddit()
    for field in temp: 
        if field not in my_list:
            sendNotification(platform, "FMF Listener", field)
            my_list.append(field)
    print(my_list)
    time.sleep(7200)
