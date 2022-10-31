from bs4 import BeautifulSoup
from lxml import etree
import urllib.request
import requests

headers = {
        'Referer': 'https://www.google.com',
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
}

base = 'https://www.hondaeastcincy.com/honda-models/'
#with urllib.request.urlopen(base) as response:
with requests.get(base, headers=headers) as response:
    html = response.text
    #print(html)
    soup = BeautifulSoup(html, 'html.parser')
    #print(soup.title.contents)
    #print(soup.body.b)
    #print(soup.find_all('a'))
    for child in soup.select('.rwd-line'):
        print(child.contents)
