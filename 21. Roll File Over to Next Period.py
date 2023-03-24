import shutil
import os
import tkinter as tk
import sys
import re
from datetime import datetime, timedelta


def roll_file_over_to_next_period(oldfilename):

    MONTH_DICT = {
        "Jan": 1,
        "Feb": 2,
        "Mar": 3,
        "Apr": 4,
        "May": 5,
        "Jun": 6,
        "Jul": 7,
        "Aug": 8,
        "Sep": 9,
        "Oct": 10,
        "Nov": 11,
        "Dec": 12,
    }

    # define regular expression patterns for MMM YYYY and ddmmyy formats
    pattern_mmm_yyyy = r"(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\s+(\d{2,4})"
    pattern_ddmmyy = r"(\d{6,8})"

    # check each pattern against the filename
    match = re.search(pattern_mmm_yyyy, oldfilename)
    if match:
        # create a new dictionary with keys and values swapped
        reverse_dict = {v: k for k, v in MONTH_DICT.items()}
        # use the value to get the corresponding key from the original dictionary
        if match.group(1) == "Dec":
            next_month = reverse_dict[1]
            year = int(match.group(2)) + 1
        else:
            next_month = reverse_dict[MONTH_DICT[match.group(1)] + 1]
            year = match.group(2)

        # replace the matched pattern with the new pattern (Aug YYYY)
        new_filename = re.sub(
            pattern_mmm_yyyy, next_month + " " + str(year), oldfilename
        )

        return new_filename
    
    else:
        match = re.search(pattern_ddmmyy, oldfilename)
        if match:
            # convert integer to string and split into year, month, and day
            date_str = str(match.group(1))
            if len(date_str) == 6:
                year = int(date_str[4:6]) + 2000
            elif len(date_str) == 8:
                year = int(date_str[4:8])
            month = int(date_str[2:4])
            day = int(date_str[:2])

            # create datetime object and format into desired date string
            date_obj = datetime(year=year, month=month, day=day)

            # Check if date is a weekend and adjust to Monday if necessary
            date_obj = date_obj + timedelta(days=1)
            if date_obj.weekday() in [5, 6]:
                date_obj += timedelta(days=7 - date_obj.weekday())

            # define list of public holidays in Victoria, Australia
            PUBLIC_HOLIDAY_2023 = [
                datetime(year=year, month=1, day=1),  # New Year's Day
                datetime(year=year, month=1, day=26),  # Australia Day
                datetime(year=year, month=3, day=14),  # Labour Day
                datetime(year=year, month=4, day=7),  # Good Friday
                datetime(year=year, month=4, day=10),  # Easter Monday
                datetime(year=year, month=4, day=25),  # ANZAC Day
                datetime(year=year, month=6, day=13),  # Queen's Birthday
                datetime(year=year, month=11, day=1),  # Melbourne Cup Day
                datetime(year=year, month=12, day=25),  # Christmas Day
                datetime(year=year, month=12, day=26),  # Boxing Day
            ]

            # check if next day is a public holiday and skip to next business day if so
            while date_obj in PUBLIC_HOLIDAY_2023:
                date_obj += timedelta(days=1)

            # format next day into desired date string
            if len(date_str) == 6:
                next_day_formatted = date_obj.strftime("%d%m%y")  # output: '260323'
            elif len(date_str) == 8:
                next_day_formatted = date_obj.strftime("%d%m%Y")  # output: '26032023'

            new_filename = re.sub(pattern_ddmmyy, next_day_formatted, oldfilename)

            return new_filename

        else:
            print(f"The filename {oldfilename} does not match any patterns.")
            return "Copy "+ oldfilename


def main():
    # create a GUI window to access the clipboard contents
    root = tk.Tk()
    root.withdraw()  # hide the root window

    # get the contents of the clipboard
    clipboard_content = root.clipboard_get()
    clipboard_content = str(clipboard_content).strip('"')

    # check if the clipboard contents is a file path
    if os.path.isfile(clipboard_content) is False:
        print("Clipboard does not contain a valid file path.")
        sys.exit()

    # get the path and filename of the selected file
    selected_file_path, selected_file_name = os.path.split(clipboard_content)

    # construct the new filename with the pattern and file extension
    new_file_name = roll_file_over_to_next_period(selected_file_name)

    # construct the path for the new file in the same folder as the original file
    new_file_path = os.path.join(selected_file_path, new_file_name)

    # copy the file to the same folder with the new name
    shutil.copy(clipboard_content, new_file_path)


if __name__ == "__main__":
    main()
