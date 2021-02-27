# === installation of the module === 

# 1) > pip install win10toast
# 2) > pip show win10toast
# 2) go to the location where win10toast was installed
# 3) replace original `__init__.py` with this version

# === modules === 

import webbrowser
import time # sleep
# from win10toast import ToastNotifier # if original win10toast was installed
from win10toast_persist import ToastNotifier # if win10toast-persist was installed

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
    "Hello World!!!",
    "Disappearing in 5 seconds...",
    duration=5) # for how many seconds toast should be visible; None = leave notification in Notification Center
time.sleep(3) # wait for 3 seconds
toaster.show_toast(
    "Example two", # title
    "Click to open URL! >>", # message 
    icon_path=None, # icon_path 
    duration=5, # for how many seconds toast should be visible; None = leave notification in Notification Center
    threaded=True, # True = run other code in parallel; False = code execution will wait till notification disappears 
    callback_on_click=open_url # click notification to run function 
    )