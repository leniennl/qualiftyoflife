import pyautogui
import time
import sys


python_window = pyautogui.getWindowsWithTitle("cmd.exe")
if len(python_window) > 1: 	sys.exit()


chrome_window = pyautogui.getWindowsWithTitle("Google Chrome")
if not chrome_window: # Check if there are any windows
    # do nothing
    pass
else:
    for window in chrome_window:
        window.activate()
        for i in range(5):
            pyautogui.click(x=3200, y=160) # Click a spot on the page
            # pyautogui.press('enter') # get rid of possible reloading warning
            time.sleep(1)
            pyautogui.hotkey("ctrl", "pagedown") # switch to the next tab
 

JDE_window = pyautogui.getWindowsWithTitle("Internet Explorer")
if not JDE_window: 
    JDE_window = pyautogui.getWindowsWithTitle("Remote")
    if not JDE_window:
        sys.exit()
for window in JDE_window:
    window.activate()
    pyautogui.press("f5")
    pyautogui.click(x=148, y=154)
    time.sleep(1)
