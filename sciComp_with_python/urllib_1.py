import urllib.request, urllib.parse, urllib.error

# Reading directly.
url = 'http://data.pr4e.org/romeo.txt'
fhand = urllib.request.urlopen(url)
for line in fhand:
    print(line.decode().strip())

print()

# Reading like a file.
fhand = urllib.request.urlopen(url)

counts = dict()
for line in fhand:
    words = line.decode().split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1
print(counts)