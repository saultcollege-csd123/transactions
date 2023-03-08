import sqlite3
from time import localtime
from time import strftime
from time import sleep

# Try running this script, and then at the same time run one of the other scripts
with sqlite3.connect('temp.db') as connection:
    cursor = connection.cursor()
    print("Starting transaction")
    cursor.execute(f"UPDATE TableA SET name = 'with-transaction-{strftime('%Y-%m-%d %H:%M:%S', localtime())}' WHERE ID = 1")
    print("Waiting 15 seconds...")
    # This will block the other scripts from running because the script is in the middle of a transaction
    sleep(15)
    cursor.execute(f"UPDATE TableB SET name = 'with-transaction-{strftime('%Y-%m-%d %H:%M:%S', localtime())}' WHERE ID = 1")
    print("Done")