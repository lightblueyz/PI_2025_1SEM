from server import  conn
from assessment import avaliar
import os


def listar(ultimo_id, media_agua, media_energia, porc_media):

    cursor = conn.cursor()

    cursor.execute("SELECT * FROM sustentabilidade WHERE id = %s", (ultimo_id,))
    sust_data = cursor.fetchone()

    cursor.execute("SELECT * FROM status WHERE id_data = %s", (ultimo_id,))
    status_data = cursor.fetchone()

    cursor.execute("SELECT * FROM media WHERE id_media = %s", (1,))
    media_data = cursor.fetchone()

    (
        _,
        _,
        energia,
        agua,
        residuos_r,
        residuos_nr,
        transporte_p,
        bicicleta,
        caminhada,
        carro_c,
        carro_e,
        carona,
    ) = sust_data

    _, sit_ener, sit_agua, sit_resid, sit_tran, sit_geral = status_data

    _, media_agua_bd, media_energia_bd, porc_media_bd = media_data

    total_residuos = residuos_r + residuos_nr
    porc = (residuos_nr / total_residuos) * 100 if total_residuos > 0 else 0

    situacao_media_litros = avaliar(media_agua_bd, 150, 200)
    situacao_media_kwh = avaliar(media_energia_bd, 5, 10)
    situacao_media_resid = avaliar(porc_media_bd, 20, 50)

    sustents = []
    nsustents = []

    if transporte_p:
        sustents.append("Transporte Público")
    if bicicleta:
        sustents.append("Bicicleta")
    if caminhada:
        sustents.append("Caminhada")

    if carro_c:
        nsustents.append("Carro Comum")
    if carro_e:
        nsustents.append("Carro Elétrico")
    if carona:
        nsustents.append("Carona")

    cursor.close()
    conn.close()

    os.system("cls")
    print("=" * 60)
    print(f"Quantidade de Água gasta por dia: {agua:.2f} L")
    print(f"   ➜ Situação: {sit_agua}\n")
    print(f"Quantidade de Energia gasta por dia: {energia:.2f} kWh")
    print(f"   ➜ Situação: {sit_ener}\n")
    print(f"Porcentagem de resíduos recicláveis: {porc:.2f} %")
    print(f"   ➜ Situação: {sit_resid}\n")
    print(
        f"Meios de Locomoção Sustentáveis: {', '.join(sustents) if sustents else 'Nenhum'}"
    )
    print(
        f"Meios de Locomoção Não Sustentáveis: {', '.join(nsustents) if nsustents else 'Nenhum'}"
    )
    print(f"   ➜ Situação: {sit_tran}\n")
    print(f"Média Geral da água: {media_agua:.2f} L")
    print(f"   ➜ Situação: {situacao_media_litros}\n")
    print(f"Média Geral da Energia: {media_energia:.2f} kWh")
    print(f"   ➜ Situação: {situacao_media_kwh}\n")
    print(f"Porcentagem Média de resíduos não recicláveis: {porc_media:.2f} %")
    print(f"   ➜ Situação: {situacao_media_resid}\n")
    print("=" * 60)
