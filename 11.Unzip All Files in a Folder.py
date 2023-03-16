#! Python3
# change OS.WALK() RAW STRING

import sys, zipfile, os

# from pathlib import Path

"""
if len(sys.argv)==1:
    print("Need Path.")
    sys.exit()
else:
    print(sys.argv[1])


path=Path(sys.argv[1])
"""

from tkinter import Tk  # py3k

# get path from clipboard
zipfilepath = Tk().selection_get(selection="CLIPBOARD")

if os.path.isdir(zipfilepath) == False:
    print("copy a valid path to clipboard")
    sys.exit()

filecounter = 0

for filefolders, subfolders, filenames in os.walk(zipfilepath):
    for filename in filenames:
        if str(filename).endswith(".zip"):
            examplezip = zipfile.ZipFile(filefolders + "/" + filename)
            examplezip.extractall(filefolders)
            examplezip.close()
            filecounter += 1


if filecounter == 0:
    print("No file to unzip in this folder.")
else:
    print(str(filecounter) + " files unzipped!")


"""
import argparse
from pathlib import Path

parser=argparse.ArgumentParser()
parser.add_argument("file_path",type=Path)

p=parser.parse_args()
print(p.file_path,type(p.file_path),p.file_path.exists())
"""
