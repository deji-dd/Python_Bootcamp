# Goal: Get title of every book with a 2* rating
import requests
import bs4

base_url = 'https://books.toscrape.com/catalogue/page-{}.html'
two_star_titles = []
for x in range(1, 51):
    res = requests.get(base_url.format(x))
    soup = bs4.BeautifulSoup(res.text, 'lxml')
    products = soup.select(".product_pod")
    for y in products:
        if y.select(".star-rating.Two"):
            two_star_titles.append(y.select('a')[1]['title'])
print(len(two_star_titles))
