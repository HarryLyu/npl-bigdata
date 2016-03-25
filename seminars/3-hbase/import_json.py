import sys
import happybase
import json
import ast

table_name = 'igor.lyubimov.user'

connection = happybase.Connection('localhost')
table = connection.table(table_name)

saved_data_fields = ['first_name', 'last_name']

for line in sys.stdin:
    user = ast.literal_eval(line)
    data = {}
    for field in saved_data_fields:
        if field in user:
            data['user_profile:' + field] = str(user[field])
    table.put(str(user['uid']), data)


for l in table.scan():
    print l