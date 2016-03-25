import sys
import re
import urlparse
import urllib

auto_users = open('auto-users.txt').read().split('\n')
auto_domains = ['cars.ru', 'avto-russia.ru', 'bmwclub.ru']

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

def is_user_is_auto (uid):
    if uid in auto_users:
        return '1'
    else:
        return '0'


for line in sys.stdin:
    data = line.strip().split("\t")
    if len(data) == 3:
        uid, date, url = data
        if is_valid_data(uid):
            domain = url2domain(url)
            if domain is not '':
                print domain + "\t" + is_user_is_auto(uid)