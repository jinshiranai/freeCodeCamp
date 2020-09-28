#!usr/bin/python3.7
# Working with APIs example program

import urllib.request, urllib.parse, urllib.error
import json

serviceuser1 = 'http://maps.googleapis.com/maps/api/geocode/json?'

while True:
    address = input('Enter location: ')
    if len(address) < 1:
        break

    url = serviceuser1 + urllib.parse.urlencode({'address': address})

    print('Retrieving', url)
    wh = urllib.request.urlopen(url)
    data = wh.read().decode()
    print('Retrieved', len(data), 'characters')

    try:
        js = json.loads(data)
    except:
        js = None

    if not js or 'status' not in js or js['status'] != 'OK':
        print('**** Failure To Retrieve ****')
        print(data)
        continue

    lat = js["results"][0]["geometry"]["location"]["lat"]
    lng = js["results"][0]["geometry"]["location"]["lng"]
    print('lat', lat, 'lng', lng)
    location = js['results'][0]['formatted_address']
    print(location)