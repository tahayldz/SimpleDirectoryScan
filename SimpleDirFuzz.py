#!/usr/bin/python3

import argparse
import requests
import sys

def Fuzz(url, file):

	if not url.startswith('http://') :
		url = 'http://' + url
	if not url.endswith('/'):
		url = url + '/'

	fh = open(file, "r")

	while True:

	 line = fh.readline()
	 line = line.rstrip('\n')
	 try:
	 	resp = requests.get(url+line)
	 except requests.ConnectionError:
	 	print("url is bad")
	 	sys.exit()
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
	try:
		Fuzz(args.u, args.w)
	except KeyboardInterrupt:
		print("by")