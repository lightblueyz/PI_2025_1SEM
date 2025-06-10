from funcions.functions_spacifics.assessment import avaliar
from db.server import conn

def get_media():

    cursor = conn.cursor()

    cursor.execute("SELECT * FROM media WHERE id_media = %s", (1,))
    media_data = cursor.fetchone()

    _, media_agua_bd, media_energia_bd, porc_media_bd = media_data

    situacao_media_litros = avaliar(media_agua_bd, 150, 200)
    situacao_media_kwh = avaliar(media_energia_bd, 5, 10)
    situacao_media_resid = avaliar(porc_media_bd, 20, 50)
    

    print("=" * 60)
    print(f"Média Geral da água: {media_agua_bd:.2f} L")
    print(f"   ➜ Situação: {situacao_media_litros}\n")
    print(f"Média Geral da Energia: {media_energia_bd:.2f} kWh")
    print(f"   ➜ Situação: {situacao_media_kwh}\n")
    print(f"Porcentagem Média de resíduos não recicláveis: {porc_media_bd:.2f} %")
    print(f"   ➜ Situação: {situacao_media_resid}\n")
    print("=" * 60)
