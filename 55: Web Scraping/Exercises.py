# Import any libraries you think you'll need to scrape a website.
import requests
import bs4

# Use requests library and BeautifulSoup to connect to http://quotes.toscrape.com/ and get the HMTL text from the homepage.
res = requests.get('http://quotes.toscrape.com/')
soup = bs4.BeautifulSoup(res.text, 'lxml')

# Get the names of all the authors on the first page.
authors = []
quotes = []
tags = []

quote = soup.select('.quote')
tag = soup.select('.tag-item')
for y in quote:
    for x in y.find_all("small", class_="author"):
        authors.append(x.text)

# Create a list of all the quotes on the first page.
for y in quote:
    for x in y.find_all("span", class_="text"):
        quotes.append(x.text)

# Inspect the site and use Beautiful Soup to extract the top ten tags from the requests text shown on the top right from the home page
for y in tag:
    for x in y.find_all("a", class_="tag"):
        tags.append(x.text)

# Use what you know about for loops and string concatenation to loop through all the pages and get all the unique authors on the website.
base_url = 'https://quotes.toscrape.com/page/{}/'
page_num = 1
unique_authors = []
while True:
    res = requests.get(base_url.format(page_num))
    soup = bs4.BeautifulSoup(res.text, 'lxml')
    unique_quote = soup.select('.quote')
    if unique_quote:
        for y in unique_quote:
            for x in y.find_all("small", class_="author"):
                if x.text not in unique_authors:
                    unique_authors.append(x.text)
        page_num += 1
    else:
        break
