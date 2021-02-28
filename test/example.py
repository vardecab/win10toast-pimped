# === installation of the module === 

# pip install win10toast-click

# === modules === 

import webbrowser
import time # time.sleep()
from win10toast_click import ToastNotifier

# === open_url function === 

page_url = 'http://example.com/'

def open_url():
    try: 
        webbrowser.open_new(page_url)
        print('Opening URL...')  
    except: 
        print('Failed to open URL. Unsupported variable type.')

# === test notification === 

toaster = ToastNotifier() # initialize
toaster.show_toast(
    "Hello World!",
    "Disappearing in 5 seconds...",
    duration=5) # for how many seconds toast should be visible; None = leave notification in Notification Center
time.sleep(3) # wait for 3 seconds
toaster.show_toast(
    "Hello World!", # title
    "Click to open URL! >>", # message 
    icon_path=None, # 'icon_path' 
    duration=5, # for how many seconds toast should be visible; None = leave notification in Notification Center
    threaded=True, # True = run other code in parallel; False = code execution will wait till notification disappears 
    callback_on_click=open_url # click notification to run function 
    )