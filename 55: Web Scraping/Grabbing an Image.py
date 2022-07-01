import requests
import bs4

res = requests.get("https://en.wikipedia.org/wiki/Deep_Blue_(chess_computer)")
soup = bs4.BeautifulSoup(res.text, 'lxml')
computer = soup.select('.thumbimage')[1]
print(computer['src'])
img_lnk = requests.get('https://upload.wikimedia.org/wikipedia/commons/thumb/8/83/One_of_Deep_Blue%27s_processors_%282586060990%29.jpg/220px-One_of_Deep_Blue%27s_processors_%282586060990%29.jpg')
f = open('image.jpg', 'wb')
f.write(img_lnk.content)
f.close()
