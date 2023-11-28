from requests_html import HTMLSession
from bs4 import BeautifulSoup

#url a extraer
s = HTMLSession()
url = 'sigof2.sofse.gob.ar/login'

def getdata(url):
    r = s.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    return soup

def getnextpage(soup):
    page = soup.find('ul', {'class': 'a-pagination'})
    if not page.find('li', {'class': 'a-disabled a-last'}):
        url = 'sigof2.sofse.gob.ar/login' + str(page.find('li', {'class': 'a-last'}).find('a')['href'])
        return url
    else:
        return None

#loop a de pagina en pagina
while True:
    soup = getdata(url)
    url = getnextpage(soup)
    if not url:
        break

print(url)