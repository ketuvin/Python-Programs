import urllib.request,urllib.parse,urllib.error

fhand = urllib.request.urlopen('http://textfiles.com/stories/fea1')
counts = dict()

for line in fhand:
    words = line.decode().split()
    for words in words:
        counts[words] = counts.get(words,0)+1

print(counts)
