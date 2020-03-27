#!/usr/bin/python3

import argparse
import requests


def Fuzz(url, file):

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

parser = argparse.ArgumentParser(description='Simple Directory Fuzz')

parser.add_argument('-u', metavar='URL', type=str,
					help='Target URL', required=False)
parser.add_argument('-w', metavar='Wordlist', type=str,
					help='Wordlist', required=False)

args = parser.parse_args()

if args.u == None or args.w == None :
	print("usage: SimpleDirFuzz.py [-h] [-u URL] [-w Wordlist]")

else:
	Fuzz(args.u, args.w)
