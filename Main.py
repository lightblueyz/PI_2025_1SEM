# Projeto Integrador Eng de Software 2025
# By: Daniel Honorato, Diogo Gonçalves Tonhosolo , Guilherme Preventi Correia , Pedro André do Carmo Chavier e Tomás Toniato

import mysql.connector
import os
from datetime import datetime

os.system("cls")

def getDtTm():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

conn = mysql.connector.connect(
    host="BD-ACD", #BD-ACD | localhost
    user="BD180225116", #BD180225116 | root
    password="Zvthd8", #Zvthd8 |
    database="BD180225116" #BD180225116 | projeto_pi    
)
cursor = conn.cursor()

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
if Tp > 1 or Tp < 0: 
    print("Inserção incorreta, Apenas 1 (Sim) ou 0 (Não)")
    Tp = int(input("Transporte Público? (1-Sim / 0-Não): ")) 
Bk = int(input("Bicicleta? (1-Sim / 0-Não): "))
if Bk > 1 or Bk < 0: 
    print("Inserção incorreta, Apenas 1 (Sim) ou 0 (Não)")
    Bk = int(input("Transporte Público? (1-Sim / 0-Não): ")) 
Cm = int(input("Caminhada? (1-Sim / 0-Não): "))
if Cm > 1 or Cm < 0: 
    print("Inserção incorreta, Apenas 1 (Sim) ou 0 (Não)")
    Cm = int(input("Transporte Público? (1-Sim / 0-Não): ")) 
Cr = int(input("Carro Comum? (1-Sim / 0-Não): "))
if Cr > 1 or Cr < 0: 
    print("Inserção incorreta, Apenas 1 (Sim) ou 0 (Não)")
    Cr = int(input("Transporte Público? (1-Sim / 0-Não): ")) 
Cre = int(input("Carro Elétrico? (1-Sim / 0-Não): "))
if Cre > 1 or Cre < 0: 
    print("Inserção incorreta, Apenas 1 (Sim) ou 0 (Não)")
    Cre = int(input("Transporte Público? (1-Sim / 0-Não): ")) 
Crn = int(input("Carona? (1-Sim / 0-Não): "))
if Crn > 1 or Crn < 0: 
    print("Inserção incorreta, Apenas 1 (Sim) ou 0 (Não)")
    Crn = int(input("Transporte Público? (1-Sim / 0-Não): ")) 



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

def avaliar(valor, baixo, moderado):
    if valor < baixo:
        return "🟢 Alta Sustentabilidade"
    elif baixo <= valor <= moderado:
        return "🟡 Sustentabilidade Moderada"
    else:
        return "🔴 Baixa Sustentabilidade"

situacaolitros = avaliar(Litros, 150, 200)
situacaokwh = avaliar(KWh, 5, 10)
situacaoporc = avaliar(porc, 20, 50)




situacao_geral = 0
sit_geral = 0   
       


insert_data = """
    INSERT INTO sustentabilidade (
        data_reg, energia, agua, residuos_r, residuos_nr, transporte_p, bicicleta, caminhada, carro_c, carro_e, carona
    ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
"""

data_values = (
    getDtTm(), Litros, KWh, Kgn, Kgr,
    Tp, Bk, Cm, Cr, Cre, Crn
)

cursor.execute(insert_data, data_values)
conn.commit()


ultimo_id = cursor.lastrowid

insert_status = """
    INSERT INTO status (
        id_data, sit_ener, sit_agua, sit_resid, sit_tran, sit_geral
    ) VALUES (%s, %s, %s, %s, %s, %s)
"""

status_values = (
    ultimo_id, situacaokwh, situacaolitros, situacaoporc, situation, situacao_geral
)

cursor.execute(insert_status, status_values)
conn.commit()





cursor.execute("SELECT SUM(energia) FROM sustentabilidade")
soma_energia = cursor.fetchone()
cursor.execute("SELECT COUNT(energia) FROM sustentabilidade")
qtd_energia = cursor.fetchone()
media_energia = soma_energia[0] / qtd_energia[0]


cursor.execute("SELECT SUM(agua) FROM sustentabilidade")
soma_agua = cursor.fetchone()
cursor.execute("SELECT COUNT(agua) FROM sustentabilidade")
qtd_agua = cursor.fetchone()
media_agua = soma_agua[0] / qtd_agua[0]

cursor.execute("SELECT SUM(residuos_r) FROM sustentabilidade")
soma_residuosR= cursor.fetchone()
cursor.execute("SELECT COUNT(residuos_r) FROM sustentabilidade")
qtd_residuosR = cursor.fetchone()
media_residuosR = soma_residuosR[0] / qtd_residuosR[0]

cursor.execute("SELECT SUM(residuos_nr) FROM sustentabilidade")
soma_residuosNR = cursor.fetchone()
cursor.execute("SELECT COUNT(residuos_nr) FROM sustentabilidade")
qtd_residuosNR = cursor.fetchone()
media_residuosNR = soma_residuosNR[0] / qtd_residuosNR[0]


if media_residuosR != 0 or media_residuosNR != 0:
    soma_media = media_residuosR + media_residuosNR
    porc_media = (media_residuosNR * 100) / soma_media
else:
    porc_media = 0
 


cursor.execute("UPDATE media SET media_agua = %s, SET media_energia = %s, SET media_residuos = %s WHERE id_media = %s",
               (media_agua, media_energia, porc_media, 1))
conn.commit()   







cursor = conn.cursor()
cursor.execute("SELECT * FROM sustentabilidade WHERE id = %s", (ultimo_id,))
sust_data = cursor.fetchone()

cursor.execute("SELECT * FROM status WHERE id_data = %s", (ultimo_id,))
status_data = cursor.fetchone()

cursor.execute("SELECT * FROM media WHERE ")

_, _, energia, agua, residuos_r, residuos_nr, transporte_p, bicicleta, caminhada, carro_c, carro_e, carona = sust_data


_, sit_ener, sit_agua, sit_resid, sit_tran, sit_geral = status_data


total_residuos = residuos_r + residuos_nr
porc = (residuos_nr / total_residuos) * 100 if total_residuos > 0 else 0


sustents = []
nsustents = []

if transporte_p: sustents.append("Transporte Público")
if bicicleta: sustents.append("Bicicleta")
if caminhada: sustents.append("Caminhada")

if carro_c: nsustents.append("Carro Comum")
if carro_e: nsustents.append("Carro Elétrico")
if carona: nsustents.append("Carona")


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
print(f"Meios de Locomoção Sustentáveis: {', '.join(sustents) if sustents else 'Nenhum'}")
print(f"Meios de Locomoção Não Sustentáveis: {', '.join(nsustents) if nsustents else 'Nenhum'}")
print(f"   ➜ Situação: {sit_tran}\n")
print(f"Média Geral da água: {media_agua:.2f} L")
print(f"   ➜ Situação: {situacao_media_litros}\n")
print(f"Média Geral da água: {media_energia:.2f} kWh")
print(f"   ➜ Situação: {situacao_media_kwh}\n")
print(f"Porcentagem Média de resíduos recicláveis: {porc_media:.2f} %")
print(f"   ➜ Situação: {situacao_media_resid}\n")
print("=" * 60)

os.system("pause")
