import mysql.connector

conn = mysql.connector.connect(
    host="localhost",  # localhost | BD-ACD
    user="root",  # root | BD180225116
    password="",  # | Zvthd8
    database="projeto_pi4",  # projeto_pi4 | BD180225116
)

cursor = conn.cursor()
