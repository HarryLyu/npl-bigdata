import sys
import happybase

table_name = 'igor.lyubimov.lab3'

connection = happybase.Connection('localhost')
table = connection.table(table_name)

for key, data in table.scan():
    print_data = [
        key,
        data['categories:2'],
        data['categories:12'],
        data['categories:13'],
        data['categories:14'],
    ]
    print "\t".join(print_data)