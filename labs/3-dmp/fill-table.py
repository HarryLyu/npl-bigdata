import sys
import happybase

table_name = 'igor.lyubimov.lab3'

connection = happybase.Connection('localhost')
table = connection.table(table_name)

categories_order = ['2', '12', '13', '14']

for line in sys.stdin:
    data = line.strip().split("\t")
    if len(data) == 2:
        hash, count = data
        uid, domain = hash.split("|")
        put_data = {}
        for cat in categories_order:
            put_data['categories:' + str(cat)] = "0"
        table.put(uid, put_data)