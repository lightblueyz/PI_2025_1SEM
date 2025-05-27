from db.server import conn
import os


def listar():
    cursor = conn.cursor(buffered=True)

    query = """
        SELECT 
            s.id, s.energia, s.agua, s.residuos_r, s.residuos_nr, 
            s.transporte_p, s.bicicleta, s.caminhada, s.carro_c, s.carro_e, s.carona,
            st.sit_ener, st.sit_agua, st.sit_resid, st.sit_tran
        FROM sustentabilidade s
        JOIN status st ON s.id = st.id_data
    """
    cursor.execute(query)
    registros = cursor.fetchall()

    for i, registro in enumerate(registros, start=1):
        (
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
            sit_ener,
            sit_agua,
            sit_resid,
            sit_tran,
        ) = registro

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

        print("=" * 60)
        print(f"Registro #{i}")
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
        print()

    
