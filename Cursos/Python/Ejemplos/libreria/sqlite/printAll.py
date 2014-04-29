
import sqlite3

conn = sqlite3.connect("mydb.db")
#conn.row_factory = sqlite3.Row
cursor = conn.cursor()

print("Printing all, ordered by artist")
for row in cursor.execute("SELECT rowid, * FROM albums ORDER BY artist"):
    print(row)
