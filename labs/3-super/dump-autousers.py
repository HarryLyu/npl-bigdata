import sys
import happybase

table_name = 'igor.lyubimov.lab3'

connection = happybase.Connection('localhost')
table = connection.table(table_name)

for key, data in table.scan():
    if data['categories:2'] == "1":
        print key