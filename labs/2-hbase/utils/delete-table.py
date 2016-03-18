#!/usr/bin/python
import happybase

table_name = 'igor.lyubimov'

connection = happybase.Connection('localhost')
print 'connected'

print connection.tables()

connection.delete_table(table_name, True)
print 'table deleted'

print connection.tables()

print 'end'