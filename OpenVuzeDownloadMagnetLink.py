#! python3
# copy a BitTorrent link from the clipboard and open it in Vuze:
# https://ww1.kickass.help/---bittorrent file can be found here

import subprocess
import pyperclip
import psutil
import time


def is_vuze_running():
    for process in psutil.process_iter():
        if "Azureus" in process.name():
            return True
    return False


# Get BitTorrent link from clipboard
bt_link = pyperclip.paste()

# Modify the link to get the megnic link
try:
    new_link = bt_link.replace("https://mylink.cx/?url=", "")
except:
    print("Paste a Magnet Link to Clipboard.")
    quit()

# Open the link in Vuze
if is_vuze_running():
    subprocess.Popen(["C:\\Program Files\\Vuze\\Azureus.exe", new_link])
else:
    print("Opening Up Vuze...")
    subprocess.Popen(["C:\\Program Files\\Vuze\\Azureus.exe"])
    time.sleep(5)
    subprocess.Popen(["C:\\Program Files\\Vuze\\Azureus.exe", new_link])

print("Link Opened by Vuze")
