import sqlite3
from time import localtime
from time import strftime
from time import sleep

with sqlite3.connect('temp.db') as connection:
    cursor = connection.cursor()
    cursor.execute(f"UPDATE TableA SET name = 'with-transaction-{strftime('%Y-%m-%d %H:%M:%S', localtime())}' WHERE ID = 1")
    sleep(15)
    cursor.execute(f"UPDATE TableB SET name = 'with-transaction-{strftime('%Y-%m-%d %H:%M:%S', localtime())}' WHERE ID = 1")