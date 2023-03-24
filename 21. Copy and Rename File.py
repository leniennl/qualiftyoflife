import shutil
import os
import tkinter as tk
import sys
import re


def generate_new_file_name(oldfilename):

    month_dict = {
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
    pattern_mmm_yyyy = r"(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\s+(\d{4})"
    pattern_ddmmyy = r"\b\d{2}\d{2}\d{2}\b"

    # check each pattern against the filename
    match = re.search(pattern_mmm_yyyy, oldfilename)
    if match:
        # extract the year from the matched pattern

        # calculate the next month (August) and format it as a 3-letter abbreviation
        # create a new dictionary with keys and values swapped
        reverse_dict = {v: k for k, v in month_dict.items()}
        # use the value to get the corresponding key from the original dictionary

        if match.group(1) == "Dec":
            next_month = reverse_dict[1]
            year = int(match.group(2)) + 1
        else:
            next_month = reverse_dict[month_dict[match.group(1)] + 1]
            year = match.group(2)

        # replace the matched pattern with the new pattern (Aug YYYY)
        new_filename = re.sub(
            pattern_mmm_yyyy, next_month + " " + str(year), oldfilename
        )

        return new_filename
    else:
        match = re.search(pattern_ddmmyy, oldfilename)
        if match:
            print(f"The filename {oldfilename} matches the ddmmyy pattern.")
        else:
            print(f"The filename {oldfilename} does not match either pattern.")



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
    new_file_name = generate_new_file_name(selected_file_name)

    # construct the path for the new file in the same folder as the original file
    new_file_path = os.path.join(selected_file_path, new_file_name)

    # copy the file to the same folder with the new name
    shutil.copy(clipboard_content, new_file_path)

    print(f"{clipboard_content} copied and renamed to {new_file_path}")


if __name__ == "__main__":
    main()


