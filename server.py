import mysql.connector

conn = mysql.connector.connect(
    host="localhost",  # BD-ACD | localhost
    user="root",  # BD180225116 | root
    password="",  # Zvthd8 |
    database="projeto_pi",  # BD180225116 | projeto_pi
)
cursor = conn.cursor()
