import os
import time
from criptografia.Criptografia import Cypher
from db.server import conn, cursor
from funcions.assessment import avaliar


def verificar_id_existe(id_):
    cursor.execute("SELECT id FROM sustentabilidade WHERE id = %s", (id_,))
    return cursor.fetchone() is not None


def atualizar_status(id_):
    cursor.execute(
        "SELECT energia, agua, residuos_r, residuos_nr, transporte_p, bicicleta, caminhada, carro_c, carro_e, carona FROM sustentabilidade WHERE id = %s",
        (id_,),
    )
    dados = cursor.fetchone()

    if not dados:
        return

    energia, agua, residuos_r, residuos_nr, tp, bk, cm, cr, cre, crn = dados

    sit_energia = avaliar(energia, 5, 10)
    sit_agua = avaliar(agua, 150, 200)

    if residuos_r != 0 or residuos_nr != 0:
        total = residuos_r + residuos_nr
        porc = (residuos_nr * 100) / total
    else:
        porc = 0
    sit_resid = avaliar(porc, 20, 50)

    sust = any([tp, bk, cm, cre])
    nsust = any([cr, crn])

    if nsust and sust:
        sit_tran = "SustentabilidadeModerada"
    elif nsust and not sust:
        sit_tran = "BaixaSustentabilidade"
    else:
        sit_tran = "AltaSustentabilidade"

    sit_geral = 0

    originallitros = sit_agua
    litroscripto = Cypher(originallitros)
    originalenergia = sit_energia
    energiacripto = Cypher(originalenergia)
    originalresiduos = sit_resid
    residuoscripto = Cypher(originalresiduos)
    originaltrans = sit_tran
    transcripto = Cypher(originaltrans)

    cursor.execute(
        """
        UPDATE status
        SET sit_ener = %s,
            sit_agua = %s,
            sit_resid = %s,
            sit_tran = %s
        WHERE id_data = %s
        """,
        (energiacripto, litroscripto, residuoscripto, transcripto, id_),
    )
    conn.commit()


def alterar_registro():
    while True:
        try:
            id_alter = int(input("Qual o ID que deseja alterar? "))
            if verificar_id_existe(id_alter):
                break
            else:
                print("ID não encontrado. Tente novamente.")
                time.sleep(2)
        except ValueError:
            print("Entrada inválida. Digite um número.")
            time.sleep(2)

    while True:
        os.system("cls")
        print("-" * 50)
        print("QUAL DADO DESEJA ALTERAR?")
        print("1- ÁGUA")
        print("2- ENERGIA")
        print("3- RESÍDUOS RECICLÁVEIS")
        print("4- RESÍDUOS NÃO RECICLÁVEIS")
        print("5- TRANSPORTE PÚBLICO")
        print("6- BICICLETA")
        print("7- CAMINHADA")
        print("8- CARRO COMUM")
        print("9- CARRO ELÉTRICO")
        print("10- CARONA")

        try:
            opcao = int(input("Digite a opção que deseja: "))
        except ValueError:
            print("Por favor, digite um número válido.")
            time.sleep(2)
            continue

        campos = {
            1: "agua",
            2: "energia",
            3: "residuos_r",
            4: "residuos_nr",
            5: "transporte_p",
            6: "bicicleta",
            7: "caminhada",
            8: "carro_c",
            9: "carro_e",
            10: "carona",
        }

        if opcao not in campos:
            print("Opção inválida. Tente novamente.")
            time.sleep(2)
            continue

        campo = campos[opcao]

        try:
            if opcao <= 4:
                novo_valor = float(input(f"Digite o novo valor para {campo.upper()}: "))
            else:
                novo_valor = int(
                    input(f"Digite 1 para SIM ou 0 para NÃO para {campo.upper()}: ")
                )
                if novo_valor not in [0, 1]:
                    raise ValueError
        except ValueError:
            print("Entrada inválida. Tente novamente.")
            time.sleep(2)
            continue

        cursor.execute(
            f"UPDATE sustentabilidade SET {campo} = %s WHERE id = %s",
            (novo_valor, id_alter),
        )
        conn.commit()

        atualizar_status(id_alter)
        print(f"{campo.upper()} atualizado com sucesso!")
        time.sleep(2)

        continuar = input("Deseja alterar outro dado? (s/n): ").strip().lower()
        if continuar != "s":
            break
