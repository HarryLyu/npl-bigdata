import sys
import happybase

table_name = 'igor.lyubimov.lab3'

connection = happybase.Connection('localhost')
table = connection.table(table_name)

categories_order = ['2', '12', '13', '14']

categories = [
    {'name': 'Autouser', 'id': 2, 'domains': ['cars.ru', 'avto-russia.ru', 'bmwclub.ru']},
    {'name': 'Designuser', 'id': 12, 'domains': ['fastpic.ru', 'fotoshkola.net', 'bigpicture.ru']},
    {'name': 'Musicuser', 'id': 13, 'domains': ['nirvana.fm', 'rusradio.ru', 'pop-music.ru']},
    {'name': 'Gadgetuser', 'id': 14, 'domains': ['snowmobile.ru', 'nastroisam.ru', 'mobyware.ru']}
]

def get_category_by_domain(domain):
    for category in categories:
        if domain in category['domains']:
            return category
    return None

for line in sys.stdin:
    data = line.strip().split("\t")
    if len(data) == 2:
        hash, count = data
        count = int(count)
        uid, domain = hash.split("|")
        if domain in categories[0]['domains'] and count >= 10:
            table.put(uid, {'categories:2': "1"})