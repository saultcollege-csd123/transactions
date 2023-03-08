import sqlite3
from time import localtime
from time import strftime

connection = sqlite3.connect('temp.db')
cursor = connection.cursor()
print("Starting updates...")
cursor.execute(f"UPDATE TableA SET name = 'no-transaction-{strftime('%Y-%m-%d %H:%M:%S', localtime())}' WHERE ID = 1")
cursor.execute(f"UPDATE TableB SET name = 'no-transaction-{strftime('%Y-%m-%d %H:%M:%S', localtime())}' WHERE ID = 1")
# Python's sqlite module automatically begins a transaction when you execute a query
# you must explicitly commit the transaction to make the changes permanent
connection.commit()
print("Done")