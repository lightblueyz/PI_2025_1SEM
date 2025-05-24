from db.server import conn
import os


def listar(id_list):
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM sustentabilidade WHERE id = %s", (id_list,))
    sust_data = cursor.fetchone()

    cursor.execute("SELECT * FROM status WHERE id_data = %s", (id_list,))
    status_data = cursor.fetchone()

    if sust_data is None or status_data is None:
        print(f"Nenhum dado encontrado para o ID {id_list}.")
        return  # <- ESSENCIAL!

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

    _, sit_ener, sit_agua, sit_resid, sit_tran, _ = status_data

    total_residuos = residuos_r + residuos_nr
    porc = (residuos_nr / total_residuos) * 100 if total_residuos > 0 else 0

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
    print("=" * 60)
