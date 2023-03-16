import bs4, requests
from pprint import pprint

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36"
}
res = requests.get(
    "http://www.bom.gov.au/vic/forecasts/scoresby.shtml", headers=headers
)
res.raise_for_status()
sweather = bs4.BeautifulSoup(res.text, "html.parser")
elms = sweather.select("div.day:nth-child(3)")

pprint(elms[0].getText())
