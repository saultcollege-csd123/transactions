import sqlite3
from time import localtime
from time import strftime

connection = sqlite3.connect('temp.db')
cursor = connection.cursor()
cursor.execute(f"UPDATE TableA SET name = 'no-transaction-{strftime('%Y-%m-%d %H:%M:%S', localtime())}' WHERE ID = 1")
cursor.execute(f"UPDATE TableB SET name = 'no-transaction-{strftime('%Y-%m-%d %H:%M:%S', localtime())}' WHERE ID = 1")
connection.commit()