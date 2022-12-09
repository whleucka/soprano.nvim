#!/usr/bin/env python3

import sys
import requests
import getopt

query = ''
argv = sys.argv[1:]
if not argv:
    exit(1)

options, remainder = getopt.getopt(sys.argv[1:], 'q:', ['query='])

for opt, arg in options:
    if opt in ('-q', '--query'):
        term = arg
if term == '':
    exit(1)

query = {'term': term}
response = requests.get("https://hleucka.ddns.net/api/v1/music/search", params=query)
data = response.json()

for datum in data['data']:
    artist = datum['artist']
    title = datum['title']
    md5 = datum['md5']
    print(f'{artist} — {title} | {md5}')
