#!usr/bin/python3.7
# XML example program 2

import xml.etree.ElementTree as ET

input = '''<stuff>
    <users>
        <user x="2">
            <id>001</id>
            <name>Jin</name>
        </user>
        <user x="7">
            <id>009</id>
            <name>Joe</name>
        </user>
    </users>
</stuff>'''

stuff = ET.fromstring(input)
lst = stuff.findall('users/user')
print('User count:', len(lst))
for item in lst:
    print('Name', item.find('name').text)
    print('Id', item.find('id').text)
    print('Attribute', item.get("x"))