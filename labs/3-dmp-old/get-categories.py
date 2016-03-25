import sys

def do_reduce(word, values):
    return word, len(values)

categories = [
    {'name': 'Autouser', 'id': 2, 'domains': [u'cars.ru', u'avto-russia.ru', u'bmwclub.ru']},
    {'name': 'Designuser', 'id': 12, 'domains': [u'fastpic.ru', u'fotoshkola.net', u'bigpicture.ru']},
    {'name': 'Musicuser', 'id': 13, 'domains': [u'nirvana.fm', u'rusradio.ru', u'pop-music.ru']},
    {'name': 'Gadgetuser', 'id': 14, 'domains': [u'snowmobile.ru', u'nastroisam.ru', u'mobyware.ru']}
]

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