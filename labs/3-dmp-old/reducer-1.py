import sys

categories = [
    {'name': 'Autouser', 'id': 2, 'domains': ['cars.ru', 'avto-russia.ru', 'bmwclub.ru']},
    {'name': 'Designuser', 'id': 12, 'domains': ['fastpic.ru', 'fotoshkola.net', 'bigpicture.ru']},
    {'name': 'Musicuser', 'id': 13, 'domains': ['nirvana.fm', 'rusradio.ru', 'pop-music.ru']},
    {'name': 'Gadgetuser', 'id': 14, 'domains': ['snowmobile.ru', 'nastroisam.ru', 'mobyware.ru']}
]

domains_by_category = {}
for category in categories:
    for domain in category['domains']:
        domains_by_category[domain] = category['id']

def dump_user(uid, visits):
    for domain in visits.keys():
        if visits[domain] > 10 and domain in domains_by_category.keys():
            print uid + "\t" + str(domains_by_category[domain])

prev_key = None
values = []

uid_visits = {}

for line in sys.stdin:
    uid, domain = line.strip().split("\t")
    if uid != prev_key and prev_key is not None:
        dump_user(uid, uid_visits)
        uid_visits = {}
    prev_key = uid
    if domain in uid_visits.keys():
        uid_visits[domain] = uid_visits[domain] + 1
    else:
        uid_visits[domain] = 1

if prev_key is not None:
    dump_user(prev_key, uid_visits)