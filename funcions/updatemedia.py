from db.server import cursor, conn

def update_media():
    
    cursor.execute("SELECT SUM(energia), COUNT(energia) FROM sustentabilidade")
    soma_energia, qtd_energia = cursor.fetchone()
    media_energia = (soma_energia or 0) / qtd_energia if qtd_energia else 0

    
    cursor.execute("SELECT SUM(agua), COUNT(agua) FROM sustentabilidade")
    soma_agua, qtd_agua = cursor.fetchone()
    media_agua = (soma_agua or 0) / qtd_agua if qtd_agua else 0

    
    cursor.execute("SELECT SUM(residuos_r), SUM(residuos_nr) FROM sustentabilidade")
    soma_r, soma_nr = cursor.fetchone()
    soma_r = soma_r or 0
    soma_nr = soma_nr or 0
    total_res = soma_r + soma_nr
    media_residuos = (soma_nr * 100) / total_res if total_res else 0

    
    cursor.execute(
        """
        UPDATE media 
        SET media_agua = %s, media_energia = %s, media_residuos = %s
        WHERE id_media = 1
    """,
        (media_agua, media_energia, media_residuos),
    )
    conn.commit()

    print("Médias atualizadas com sucesso!")
