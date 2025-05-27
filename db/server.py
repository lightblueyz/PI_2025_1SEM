import mysql.connector

conn = mysql.connector.connect(
    host="BD-ACD",  # BD-ACD | localhost
    user="BD180225116",  # BD180225116 | root
    password="Zvthd8",  # Zvthd8 |
    database="BD180225116",  # BD180225116 | projeto_pi2
)
cursor = conn.cursor()
