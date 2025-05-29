from db.server import cursor, conn
from funcions.updatemedia import update_media

def delete(id_remove):
    
    while True:   
        try:
            cursor.execute("DELETE FROM status WHERE id_data = %s", (id_remove,))
            cursor.execute("DELETE FROM sustentabilidade WHERE id = %s", (id_remove,))
            conn.commit()
            update_media()
            print(f"Registro {id_remove} removido e média atualizada com sucesso.")
            break
        except:
            print(f"Id incorreto")    
