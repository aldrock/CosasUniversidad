import sqlite3

conn = sqlite3.connect("mydb.db")
cursor = conn.cursor()

sql_req = """
UPDATE albums
SET artist = 'Avicii=D'
WHERE artist = 'Avicii'
"""
cursor.execute(sql_req)
conn.commit()
