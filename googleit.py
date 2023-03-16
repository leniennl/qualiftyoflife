#! python3
# googleIt.py - lauch Google search from the command line or clipboard.

import webbrowser, sys, pyperclip, requests, bs4
from bs4 import BeautifulSoup


if len(sys.argv) > 1:
    # Get address from command line.
    search = sys.argv[1:]
    stufftogoogle = "+".join(sys.argv[1:])

else:

    if " " in pyperclip.paste():
        search = pyperclip.paste()
        stufftogoogle = pyperclip.paste().replace(" ", "+")
    else:
        stufftogoogle = pyperclip.paste()
        search = pyperclip.paste()


webbrowser.open("https://www.google.com/search?q=" + stufftogoogle)

results = 1  # valid options 10, 20, 30, 40, 50, and 100
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; rv:107.0) Gecko/20100101 Firefox/107.0"
}


page = requests.get(f"https://www.google.com/search?q={search}&num={results}")
page.raise_for_status()

soup = BeautifulSoup(page.content, "html.parser")
links = soup.findAll("a")

counter = 0
for link in links:
    link_href = link.get("href")
    if (
        "url?q=" in link_href
        and not "webcache" in link_href
        and not "%" in link_href
        and counter < 2
    ):
        print("Opening: " + link.get("href").split("?q=")[1].split("&sa=U")[0])
        webbrowser.open(link.get("href").split("?q=")[1].split("&sa=U")[0])
        counter += 1
