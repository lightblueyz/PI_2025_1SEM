import mysql.connector

conn = mysql.connector.connect(
    conn = mysql.connector.connect(
    host="localhost",  # ou "BD-ACD"
    user="root",       # ou "BD180225116"
    password="",       # ou "Zvthd8"
    database="projeto_pi4"  # ou "BD180225116"
)
)
cursor = conn.cursor()
