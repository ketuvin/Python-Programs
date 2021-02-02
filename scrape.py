import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

#Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#Website URL
url = 'https://www.businessinsider.com/video-games-2018-list-2017-12'
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

print('\nList of Games: (DATA #1)\n')
# Retrieve and print all of the h2 tags
for i, h2 in enumerate(soup.select('h2')):
    print(h2.text)

print('\nCompany of Games: (DATA #2)\n')
# Retrieve and print all of the span tags
for i, span in enumerate(soup.find_all('span', {'class':'image-source'})):
    print(i, span.text)
