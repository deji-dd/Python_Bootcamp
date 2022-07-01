import requests
import bs4

res = requests.get("https://en.wikipedia.org/wiki/Grace_Hopper")
soup = bs4.BeautifulSoup(res.text, 'lxml')
items = soup.select('.toctext')
for x in items:
    print(x.text)

