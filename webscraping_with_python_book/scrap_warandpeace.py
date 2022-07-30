from urllib.request import urlopen
from bs4 import BeautifulSoup

url = 'https://pythonscraping.com/pages/warandpeace.html'
html = urlopen(url)
bs = BeautifulSoup(html.read(), 'html.parser')

nameList = bs.find_all('span', {'class':'green'})
for name in nameList:
    print(name.get_text())