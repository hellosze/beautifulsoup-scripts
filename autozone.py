from bs4 import BeautifulSoup
from lxml import etree
import urllib.request

url = 'https://www.autozone.com/brakes-and-traction-control/brake-pads?filterByKeyWord=brake+pads&fromString=search&isIgnoreVehicle=false&newYmme=true'

req = urllib.request.Request(
    url, 
    data=None, 
    headers={
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
    }
)
html = urllib.request.urlopen(req).read()
print(html)
soup = BeautifulSoup(html, 'html.parser')
print(soup.prettify())
    #print(soup.title.contents)
    #print(soup.body.b)
    #print(soup.find_all('a'))
for child in soup.select('.az_UIb az_fy img#productImage'):
	print(child['src'])
        #href = child['href']
        #abs_url = urllib.parse.urljoin(base, href)
        #print(abs_url)
