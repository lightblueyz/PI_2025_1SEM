import os
from db.server import cursor, conn
from funcions.assessment import avaliar
from funcions.updatemedia import update_media
from funcions.validacao_transporte import (
    tp_val,
    bk_val,
    cm_val,
    cr_val,
    cre_val,
    crn_val,
)
from funcions.validacao_parametros import (
    litros_val,
    kwh_val,
    kgn_val,
    kgr_val
)




os.system("cls")


def validacao():
    while True:
        try:
            loop = int(input("Deseja algo mais? (1)SIM | (2)NÃO: "))
            if loop == 1 or loop == 2:
                return loop
            else:
                print("Opção inválida. Digite 1 para SIM ou 2 para NÃO.")
        except ValueError:
            print("Entrada inválida. Digite um número (1 ou 2).")


def cadastro(date):
    print("=" * 60)
    print(f"{'ANÁLISE DE SUSTENTABILIDADE':^60}")
    print("=" * 60)
    print(f"Data e Hora: {date}")
    print("=" * 60)

    Litros = litros_val()
    KWh = kwh_val()
    Kgn = kgn_val()
    Kgr = kgr_val()

    print("\nMeios de Transporte Utilizados:")

    Tp = tp_val()
    Bk = bk_val()
    Cm = cm_val()
    Cr = cr_val()
    Cre = cre_val()
    Crn = crn_val()

    sustents = []
    nsustents = []

    if Tp:
        sustents.append("Transporte Público")
    if Bk:
        sustents.append("Bicicleta")
    if Cm:
        sustents.append("Caminhada")
    if Cre:
        sustents.append("Carro Elétrico")
    if Cr:
        nsustents.append("Carro Comum")
    if Crn:
        nsustents.append("Carona")

    sust = any([Tp, Bk, Cm, Cre])
    sustn = any([Cr, Crn])

    if sustn and sust:
        situation = "🟡 Sustentabilidade Moderada"
    elif sustn and not sust:
        situation = "🔴 Baixa Sustentabilidade"
    else:
        situation = "🟢 Alta Sustentabilidade"

    if Kgr != 0 or Kgn != 0:
        soma = Kgr + Kgn
        porc = (Kgn * 100) / soma
    else:
        porc = 0

    situacaolitros = avaliar(Litros, 150, 200)
    situacaokwh = avaliar(KWh, 5, 10)
    situacaoporc = avaliar(porc, 20, 50)

    situacao_geral = 0

    insert_data = """
        INSERT INTO sustentabilidade (
            data_reg, energia, agua, residuos_r, residuos_nr, transporte_p, bicicleta, caminhada, carro_c, carro_e, carona
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """

    data_values = (date, KWh, Litros, Kgr, Kgn, Tp, Bk, Cm, Cr, Cre, Crn)

    cursor.execute(insert_data, data_values)
    conn.commit()

    ultimo_id = cursor.lastrowid

    insert_status = """
        INSERT INTO status (
            id_data, sit_ener, sit_agua, sit_resid, sit_tran, sit_geral
        ) VALUES (%s, %s, %s, %s, %s, %s)
    """

    status_values = (
        ultimo_id,
        situacaokwh,
        situacaolitros,
        situacaoporc,
        situation,
        situacao_geral,
    )

    cursor.execute(insert_status, status_values)
    conn.commit()

    cursor.execute("SELECT SUM(energia) FROM sustentabilidade")
    soma_energia = cursor.fetchone()
    cursor.execute("SELECT COUNT(energia) FROM sustentabilidade")
    qtd_energia = cursor.fetchone()
    media_energia = soma_energia[0] / qtd_energia[0] if qtd_energia[0] else 0

    cursor.execute("SELECT SUM(agua) FROM sustentabilidade")
    soma_agua = cursor.fetchone()
    cursor.execute("SELECT COUNT(agua) FROM sustentabilidade")
    qtd_agua = cursor.fetchone()
    media_agua = soma_agua[0] / qtd_agua[0] if qtd_agua[0] else 0

    cursor.execute("SELECT SUM(residuos_r) FROM sustentabilidade")
    soma_residuosR = cursor.fetchone()
    cursor.execute("SELECT COUNT(residuos_r) FROM sustentabilidade")
    qtd_residuosR = cursor.fetchone()
    media_residuosR = soma_residuosR[0] / qtd_residuosR[0] if qtd_residuosR[0] else 0

    cursor.execute("SELECT SUM(residuos_nr) FROM sustentabilidade")
    soma_residuosNR = cursor.fetchone()
    cursor.execute("SELECT COUNT(residuos_nr) FROM sustentabilidade")
    qtd_residuosNR = cursor.fetchone()
    media_residuosNR = (
        soma_residuosNR[0] / qtd_residuosNR[0] if qtd_residuosNR[0] else 0
    )

    soma_media = media_residuosR + media_residuosNR
    if soma_media > 0:
        porc_media = (media_residuosNR * 100) / soma_media
    else:
        porc_media = 0

    update_media()

    return ultimo_id, media_agua, media_energia, porc_media
