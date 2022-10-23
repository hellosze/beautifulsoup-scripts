from bs4 import BeautifulSoup
from lxml import etree
import urllib.request

base = 'hhttps://en.m.wikipedia.org/wiki/Linus_Torvalds'
with urllib.request.urlopen(base) as response:
    html = response.read()
    soup = BeautifulSoup(html, 'html.parser')
    print(soup)
    #print(soup.title.contents)
    #print(soup.body.b)
    #print(soup.find_all('a'))
    #for child in soup.select('font.ftitle a'):
        #print(child.contents)
        #href = child['href']
        #abs_url = urllib.parse.urljoin(base, href)
        #print(abs_url)
