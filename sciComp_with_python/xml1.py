#!usr/bin/python3.7
# XML example program.

import xml.etree.ElementTree as ET

data = '''<person>
    <name>Jin</name>
    <phone type="intl">
        +1 234 567 9810
    </phone>
    <email hide="yes"/>
</person>'''

tree = ET.fromstring(data)
print('Name:',tree.find('name').text)
print('Attr:',tree.find('email').get('hide'))