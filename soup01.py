from bs4 import BeautifulSoup
import urllib.request

base = 'https://www.python.org'
with urllib.request.urlopen('https://www.python.org') as response:
    html = response.read()
    soup = BeautifulSoup(html, 'html.parser')
    print(soup.title.contents)
    #print(soup.body.b)
    #print(soup.find_all('a'))
    for child in soup.find_all('a'):
        #print(child.contents)
        href = child['href']
        abs_url = urllib.parse.urljoin(base, href)
        print(abs_url)
