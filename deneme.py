#!/usr/bin/python3

import argparse
import requests

url = 'http://10.10.10.175/'
file = 'text.txt'

if not url.startswith('http://') :
	url = 'http://' + url
if not url.endswith('/'):
	url = url + '/'

fh = open(file, "r")

while True:

	line = fh.readline()

	resp = requests.get(url+line)
 
	if not line:
		break
 
	if not resp.status_code == 404:
		print(str(resp.status_code)+"\t"+url+line)


fh.close()