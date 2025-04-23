import mysql.connector
from datetime import datetime
import os

os.system("cls")

def getDtTm():
    data_atual = datetime.now().strftime("%Y-%m-%d")

# Conexão com o banco
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="tua_senha_aqui",
    database="sustentabilidadeDB"
)
cursor = conn.cursor()

# Coleta de dados
print("=" * 60)
print(f"{'ANÁLISE DE SUSTENTABILIDADE':^60}")
print("=" * 60)
print(f"Data e Hora: {getDtTm()}")
print("=" * 60)

Litros = float(input("Quantidade de Água gasta (L): "))
KWh = float(input("Quantidade de Energia Elétrica (kWh): "))
Kgn = float(input("Quantidade de Resíduos não recicláveis (Kg): "))
Kgr = float(input("Quantidade de Resíduos recicláveis (Kg): "))

print("\nMeios de Transporte Utilizados:")
Tp = int(input("Transporte Público? (1-Sim / 0-Não): "))
Bk = int(input("Bicicleta? (1-Sim / 0-Não): "))
Cm = int(input("Caminhada? (1-Sim / 0-Não): "))
Cr = int(input("Carro Comum? (1-Sim / 0-Não): "))
Cre = int(input("Carro Elétrico? (1-Sim / 0-Não): "))
Crn = int(input("Carona? (1-Sim / 0-Não): "))

# Inserção no banco
query = """
    INSERT INTO monitoramentos (
        data_hora, agua, energia, residuos_nao_reciclaveis, residuos_reciclaveis,
        transporte_publico, bicicleta, caminhada, carro, carro_eletrico, carona
    ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
"""
values = (
    getDtTm(), Litros, KWh, Kgn, Kgr,
    Tp, Bk, Cm, Cr, Cre, Crn
)

cursor.execute(query, values)
conn.commit()

print("\n✅ Dados inseridos com sucesso no banco de dados!")

cursor.close()
conn.close()
