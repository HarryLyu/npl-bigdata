import sys
import re
import urlparse
import urllib

def url2domain(url):
   try:
       a = urlparse.urlparse(urllib.unquote(url.strip()))
       if (a.scheme in ['http','https']):
           b = re.search("(?:www\.)?(.*)",a.netloc).group(1)
           if b is not None:
               return str(b).strip()
           else:
               return ''
       else:
           return ''
   except:
       return

def is_valid_data (data):
    return data != '' and data != '-'

def is_valid_url (data):
    return data.startswith('http%3A//') or data.startswith('https%3A//')

for line in sys.stdin:
    data = line.strip().split("\t")
    if len(data) == 3:
        uid, date, url = data
        if is_valid_data(uid):
            domain = url2domain(url)
            if domain is not '':
                print uid + '|' + domain + "\t1"