import requests
import bs4

result = requests.get('http://example.com/')
soup = bs4.BeautifulSoup(result.text, 'lxml')
print(soup.select('title')[0].getText())
site_p = soup.select('p')
for x in site_p:
    print(x.getText())
