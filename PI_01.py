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
Bk = int(input("Bicicleta? (1-Sim / 0-Não): "))
Cm = int(input("Caminhada? (1-Sim / 0-Não): "))
Cr = int(input("Carro Comum? (1-Sim / 0-Não): "))
Cre = int(input("Carro Elétrico? (1-Sim / 0-Não): "))
Crn = int(input("Carona? (1-Sim / 0-Não): "))


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




situacao_geral = ""
media_L = 0
media_E = 0
media_R = 0 
media_T = 0 

media_arr = []


if situacaolitros == "🟢 Alta Sustentabilidade": 
    media_L += 1
    media_arr.append(media_L)
elif situacaolitros == "🟡 Sustentabilidade Moderada": 
    media_L = 0
    media_arr.append(media_L)
else: 
    media_L -=1
    media_arr.append(media_L) 
 

if situacaokwh == "🟢 Alta Sustentabilidade": 
    media_E += 1
    media_arr.append(media_E)
elif situacaokwh == "🟡 Sustentabilidade Moderada": 
    media_E = 0
    media_arr.append(media_E)
else: 
    media_E -=1
    media_arr.append(media_E)            


if situacaoporc == "🟢 Alta Sustentabilidade": 
    media_R += 1
    media_arr.append(media_R)
elif situacaoporc == "🟡 Sustentabilidade Moderada": 
    media_R = 0
    media_arr.append(media_R)
else: 
    media_R -=1
    media_arr.append(media_R)   

if situation == "🟢 Alta Sustentabilidade": 
    media_T += 1
    media_arr.append(media_T)
elif situation == "🟡 Sustentabilidade Moderada": 
    media_T = 0
    media_arr.append(media_T)
else: 
    media_T -=1
    media_arr.append(media_T)       
    
 

soma_arr = sum(media_arr)


if soma_arr > 0: 
    situacao_geral = ("🟢 Alta Sustentabilidade")
elif soma_arr < 0: 
    situacao_geral = ("🔴 Baixa Sustentabilidade")
else: 
    situacao_geral =  ("🟡 Sustentabilidade Moderada")       
   
    



query = """
    INSERT INTO sustentabilidade (
        data_reg, energia, agua, residuos_r, residuos_nr, transporte_p, bicicleta, caminhada, carro_c, carro_e, carona
    ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
"""

values = (
    getDtTm(), Litros, KWh, Kgn, Kgr,
    Tp, Bk, Cm, Cr, Cre, Crn
)

cursor.execute(query, values)
conn.commit()

ultimo_id = cursor.lastrowid

query2 = """
    INSERT INTO status (
        id_data, sit_ener, sit_agua, sit_resid, sit_tran, sit_geral
    ) VALUES (%s, %s, %s, %s, %s, %s)
"""

values2 = (
    ultimo_id, situacaokwh, situacaolitros, situacaoporc, situation, situacao_geral
)

cursor.execute(query2, values2)
conn.commit()


cursor = conn.cursor()
cursor.execute("SELECT * FROM sustentabilidade WHERE id = %s", (ultimo_id,))
sust_data = cursor.fetchone()

cursor.execute("SELECT * FROM status WHERE id_data = %s", (ultimo_id,))
status_data = cursor.fetchone()

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



print("\n" + "=" * 60)
print(f"Quantidade de Água gasta por dia: {agua:.2f} L")
print(f"   ➜ Situação: {sit_agua}\n")
print(f"Quantidade de Energia gasta por dia: {energia:.2f} kWh")
print(f"   ➜ Situação: {sit_ener}\n")
print(f"Porcentagem de resíduos não recicláveis: {porc:.2f} %")
print(f"   ➜ Situação: {sit_resid}\n")
print(f"Meios de Locomoção Sustentáveis: {', '.join(sustents) if sustents else 'Nenhum'}")
print(f"Meios de Locomoção Não Sustentáveis: {', '.join(nsustents) if nsustents else 'Nenhum'}")
print(f"   ➜ Situação: {sit_tran}\n")
print(f"Média Geral: {sit_geral}")
print("=" * 60)


os.system("pause")
