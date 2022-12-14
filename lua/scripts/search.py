#!/usr/bin/env python3

import sys
import requests
import getopt

query = ''
argv = sys.argv[1:]
if not argv:
    exit(1)

options, remainder = getopt.getopt(argv, 'q:', ['query='])

for opt, arg in options:
    if opt in ('-q', '--query'):
        term = arg
if term == '':
    exit(1)

query = {'term': term}
response = requests.get("https://hleucka.ddns.net/api/v1/music/search", params=query)
data = response.json()

for datum in data['data']:
    print(f'{datum["artist"]} — {datum["title"]} | {datum["md5"]}')
