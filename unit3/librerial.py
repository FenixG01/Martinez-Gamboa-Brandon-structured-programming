import mysql.connector

try:
    conexion = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="inventary"
    )
    cursor = conexion.cursor()
except mysql.connector.Error:
    exit()

def ver_libros():
    cursor.execute("SELECT * FROM producto")
    libros = cursor.fetchall()
    for lib in libros:
        print(f"ID: {lib[0]} | Título: {lib[1]} | Año: {lib[2]} | Autor: {lib[3]}")

def subir_libro():
    titulo = input("Título: ")
    anio = int(input("Año: "))
    autor = input("Autor: ")
    sql = "INSERT INTO producto (nam, num, descr) VALUES (%s, %s, %s)"
    cursor.execute(sql, (titulo, anio, autor))
    conexion.commit()
    print("Subido.")

def borrar_libro():
    id_libro = int(input("ID a eliminar: "))
    cursor.execute("DELETE FROM producto WHERE id = %s", (id_libro,))
    conexion.commit()
    print("Eliminado.")

subir_libro()
borrar_libro()
ver_libros()

cursor.close()
conexion.close()