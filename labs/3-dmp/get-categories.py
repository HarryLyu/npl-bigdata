import sys

def do_reduce(word, values):
    return word, len(values)

categories = [
    {'name': 'Autouser', 'id': 2, 'domains': ['cars.ru', 'avto-russia.ru', 'bmwclub.ru']},
    {'name': 'Designuser', 'id': 12, 'domains': ['fastpic.ru', 'fotoshkola.net', 'bigpicture.ru']},
    {'name': 'Musicuser', 'id': 13, 'domains': ['nirvana.fm', 'rusradio.ru', 'pop-music.ru']},
    {'name': 'Gadgetuser', 'id': 14, 'domains': ['snowmobile.ru', 'nastroisam.ru', 'mobyware.ru']}
]

def get_category_by_domain(domain):
    for category in categories:
        if domain in category['domains']:
            return category['id']
    return None

prev_key = None
values = []

for line in sys.stdin:
    uid, count = line.strip().split("\t")
    if uid != prev_key and prev_key is not None:
        result_key, result_value = do_reduce(prev_key, values)
        if result_value > 1:
            print(result_key + "\t" + str(result_value))
        values = []
    prev_key = uid
    values.append(count)

if prev_key is not None:
    result_key, result_value = do_reduce(prev_key, values)
    print(result_key + "\t" + str(result_value))