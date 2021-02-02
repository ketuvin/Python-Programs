import urllib.request,urllib.parse,urllib.error

url = 'https://en.wikipedia.org/wiki/Page'
fhand = urllib.request.urlopen(url)

for line in fhand:
    print (line.decode().split())
