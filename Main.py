# Projeto Integrador Eng de Software 2025
# By: Daniel Honorato, Diogo Gonçalves Tonhosolo , Guilherme Preventi Correia , Pedro André do Carmo Chavier e Tomás Toniato


import os
from datetime import datetime
from post import cadastro
from get import listar


os.system("cls")


def getDtTm():
    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return date


date = getDtTm()


print("=" * 60)
print(f"{'ANÁLISE DE SUSTENTABILIDADE':^60}")
print("=" * 60)
print(f"Data e Hora: {date}")
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


# POST


cadastro(KWh, Litros, Kgr, Kgn, Tp, Bk, Cm, Cr, Cre, Crn, date)
ultimo_id, media_agua, media_energia, porc_media = cadastro(
    KWh, Litros, Kgr, Kgn, Tp, Bk, Cm, Cr, Cre, Crn, date
)

# LIST


listar(ultimo_id, media_agua, media_energia, porc_media)


os.system("pause")
