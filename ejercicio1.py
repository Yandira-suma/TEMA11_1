
import sqlite3

conn = sqlite3.connect("alumnos.db")
cursor = conn.cursor()


cursor.execute("""
CREATE TABLE IF NOT EXISTS Alumnos (
  id INTEGER PRIMARY KEY,
  nombre TEXT,
  apellido TEXT
)
""")


cursor.execute("INSERT INTO Alumnos VALUES (1, 'Milagros', 'Baca')")
cursor.execute("INSERT INTO Alumnos VALUES (2, 'María', 'flores')")
cursor.execute("INSERT INTO Alumnos VALUES (3, 'Galiano', 'Martínez')")
cursor.execute("INSERT INTO Alumnos VALUES (4, 'Lupe', 'Sanchez')")
cursor.execute("INSERT INTO Alumnos VALUES (5, 'Amanda', 'Sánchez')")
cursor.execute("INSERT INTO Alumnos VALUES (6, 'Marta', 'Espinoza')")
cursor.execute("INSERT INTO Alumnos VALUES (7, 'Angel', 'Casas')")
cursor.execute("INSERT INTO Alumnos VALUES (8, 'Jordy', 'Nina')")

# realizar búsqueda
cursor.execute("SELECT * FROM Alumnos WHERE nombre = 'Milagros'")
resultado = cursor.fetchone()

print("ID:", resultado[0])
print("Nombre:", resultado[1])
print("Apellido:", resultado[2])


conn.commit()
conn.close()