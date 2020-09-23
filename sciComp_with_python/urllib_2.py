import urllib.request, urllib.parse, urllib.error

#url = 'http://www.dr-chuck.com/page1.htm'
url = 'https://manabi-zoo.herokuapp.com'

fhand = urllib.request.urlopen(url)
for line in fhand:
    print(line.decode().strip())