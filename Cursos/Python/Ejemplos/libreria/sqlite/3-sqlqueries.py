import sqlite3

conn = sqlite3.connect("mydb.db")
#conn.row_factory = sqlite3.Row
#Con esta linea los resultados seran de tipo "Row" que se pueden acceder como diccionarios (pero no cambiar)
cursor = conn.cursor()

#Seleccionando
print("\nSeleccionando selectivo\n")
sql = "SELECT * FROM albums WHERE artist=?"
cursor.execute(sql, [("Red")])

print(cursor.fetchall())  # tambien se puede fetchone()
#SOLO se puede hacer fetch* una vez

#Descomentar esta si esta en modo "Row"
#for row in cursor.fetchall():
    #print("Artista: %s, Titulo: %s" %(row["artist"], row["title"]))

print("\nTodo ordenado por artista\n")
for row in cursor.execute("SELECT rowid, * FROM albums ORDER BY artist"):
    #Descomentar esta si esta en modo "Row"
    #print("Artista: %s, Titulo: %s" %(row["artist"], row["title"]))
    print(row)

print("\nUsando \"LIKE\" query ;-)\n")
sql = """
SELECT * FROM albums
WHERE title LIKE 'THE%'
"""
cursor.execute(sql)
#print(cursor.fetchall()) #Ahora vamos a usar fetchone()
a = cursor.fetchone()
while a:
    print(a)
    #Descomentar esta si esta en modo "Row"
    #print("Artista: %s, Titulo: %s" %(a["artist"], a["title"]))
    a = cursor.fetchone()
