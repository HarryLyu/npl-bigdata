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

categories = [
    {'name': 'Autouser', 'id': 2, 'domains': [u'cars.ru', u'avto-russia.ru', u'bmwclub.ru']},
    {'name': 'Designuser', 'id': 12, 'domains': [u'fastpic.ru', u'fotoshkola.net', u'bigpicture.ru']},
    {'name': 'Musicuser', 'id': 13, 'domains': [u'nirvana.fm', u'rusradio.ru', u'pop-music.ru']},
    {'name': 'Gadgetuser', 'id': 14, 'domains': [u'snowmobile.ru', u'nastroisam.ru', u'mobyware.ru']}
]

domains = []
for category in categories:
    domains.extend(category['domains'])

for line in sys.stdin:
    data = line.strip().split("\t")
    if len(data) == 3:
        uid, date, url = data
        if is_valid_data(uid) and is_valid_url(url):
            domain = url2domain(url)
            print uid + '\t' + domain
