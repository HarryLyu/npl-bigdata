#!/usr/bin/python
import happybase

table_name = 'igor.lyubimov'

connection = happybase.Connection('localhost')
print 'connected'

print connection.tables()

cfs = {'column': {'max_versions': 4096}}
connection.create_table(table_name, families = cfs)
print 'table created'

print connection.tables()

print 'end'