from db.server import cursor, conn
from funcions.updatemedia import update_media

def delete():

    while True:   
        try:
            id_remove = int(input("Digite o ID que deseja remover: "))
            
            cursor.execute("DELETE FROM status WHERE id_data = %s", (id_remove,))
            cursor.execute("DELETE FROM sustentabilidade WHERE id = %s", (id_remove,))
            
            conn.commit()
            update_media()
            
            print(f"Registro {id_remove} removido e média atualizada com sucesso.")
            break
        
        except ValueError:
            print("ID inválido. Digite um número inteiro.") 
                
