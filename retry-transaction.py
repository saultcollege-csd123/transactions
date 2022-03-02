import sqlite3
from time import localtime
from time import strftime
from time import sleep

MAX_TRIES = 5
tries = 1
while tries < MAX_TRIES:
    try:
        with sqlite3.connect('temp.db') as connection:
            cursor = connection.cursor()
            cursor.execute(f"UPDATE TableA SET name = 'with-transaction-{strftime('%Y-%m-%d %H:%M:%S', localtime())}' WHERE ID = 1")
            cursor.execute(f"UPDATE TableB SET name = 'with-transaction-{strftime('%Y-%m-%d %H:%M:%S', localtime())}' WHERE ID = 1")
            break # Stop retrying
    except sqlite3.OperationalError:
        tries += 1
        print("Transaction could not complete... retrying...")

if tries == MAX_TRIES:
    print("Could not complete transaction")
