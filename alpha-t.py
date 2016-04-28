import urllib2

def fetch_url(url, params, method):
    ua="Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0)"
    cookie="a=a"
    proxy="127.0.0.1:8080"

    # Explicitly set proxy
    proxy=urllib2.ProxyHandler({'http': proxy})
    opener=urllib2.build_opener(proxy)
    urllib2.install_opener(opener)

    #params = urllib2.urlencode(params)
    if method=='POST':
        # Setup a request object with customer headers
        r=urllib2.Request(url)
        r.add_header('User-Agent', ua)
        r.add_header('Cookie', cookie)
        f=urllib2.urlopen(r, params)
    else:
        # Setup a request object with customer headers
        r = urllib2.Request(url)
        r.add_header('User-Agent', ua)
        r.add_header('Cookie', cookie)
        f=urllib2.urlopen(r)
        return (f.read())

def match_resp(hay, needle):
    m=hay.find(needle)
    if m != -1:
        return True
    else:
        return False

if __name__ == "__main__":
    #main(sys.argv[1:])
    resp=fetch_url("http://www.google.com?a=b",False, "GET")
    m=match_resp(resp,"Google")
    if m:
        print True
    else:
        print False
    print m
    #fetch_url("http://www.google.com", "a=a%3db", "POST")
