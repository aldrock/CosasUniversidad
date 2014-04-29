import sqlite3

conn = sqlite3.connect("mydb.db")
cursor = conn.cursor()

sql_req = """
DELETE FROM albums
WHERE artist = 'Andy Hunter'
"""
cursor.execute(sql_req)
conn.commit()
