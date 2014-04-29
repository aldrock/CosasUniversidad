import sqlite3

#Se conecta
conn = sqlite3.connect("mydb.db")

#Se crea un cursor para poder interactuar
cursor = conn.cursor()

#Se crea la tabla
cursor.execute("""CREATE TABLE IF NOT EXISTS albums
                    (title text, artist text, release_date text,
                    publisher text, media_type text)
        """)
#Los tipos de datos son: null, integer, real, text y blob

#Insertemos una entrada
cursor.execute("INSERT INTO albums VALUES ('True', 'Avicii', '2/2/2013', 'Ni idea Records', 'MP3')")

#Hay que guardar los datos
conn.commit()

#Se puede insertar muchos con los parametros ? y un array de iterables
albums = [('Exodus', 'Andy Hunter', '7/9/2002', 'Sparrow Records', 'CD'),
        ('Until We Have Faces', 'Red', '2/1/2011', 'Essential Records', 'CD'),
        ('The End is Where We Begin', 'Thousand Foot Krutch', '4/17/2012', 'TFKmusic', 'CD'),
        ('The Good Life', 'Trip Lee', '4/10/2012', 'Reach Records', 'CD')]

#Hacemos uso de executemany (Se usa ? en lugar de %s para evitar posibles SQL injections, aunque nunca nada es 100% seguro)
cursor.executemany("INSERT INTO albums VALUES (?,?,?,?,?)", albums)

#Guardar datos again
conn.commit()
