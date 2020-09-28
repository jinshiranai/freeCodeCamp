#!usr/bin/python3.7
# Example JSON program 1.

import json

data = '''{
    "name" : "Jin",
    "phone" : {
        "type" : "intl",
        "number" : "+1 234 567 9810"
    },
    "email" : {
        "hide" : "yes"
    }
}'''

info = json.loads(data)
print('Name:',info["name"])
print('Hide:',info["email"]["hide"])