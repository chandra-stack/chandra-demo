#!/usr/bin/env python
import json
f=open(file=".github/workflows/config.json", mode='r')
parser=json.load(f)
print('BUILD-URL :',parser['name'])
print('BUILD-BODY :',parser['body'])
f.close()
