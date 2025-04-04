# Projeto Integrador Eng de Software 2025
# By: Daniel Honorato, Diogo Gonçalves Tonhosolo , Guilherme Preventi Correia , Pedro André do Carmo Chavier e Tomás Toniato

import os
from datetime import datetime

os.system("cls")

def getDtTm():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

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

if Tp: sustents.append("Transporte Público")
if Bk: sustents.append("Bicicleta")
if Cm: sustents.append("Caminhada")
if Cre: sustents.append("Carro Elétrico")
if Cr: nsustents.append("Carro Comum")
if Crn: nsustents.append("Carona")

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
situacaoporc = avaliar(porc, 20, 50)
situacaokwh = avaliar(KWh, 5, 10)

print("\n" + "=" * 60)
print(f"Quantidade de Água gasta por dia: {Litros:.2f} L")
print(f"   ➜ Situação: {situacaolitros}\n")
print(f"Quantidade de Energia gasta por dia: {KWh:.2f} kWh")
print(f"   ➜ Situação: {situacaokwh}\n")
print(f"Porcentagem de resíduos não recicláveis: {porc:.2f} %")
print(f"   ➜ Situação: {situacaoporc}\n")
print(f"Meios de Locomoção Sustentáveis: {', '.join(sustents) if sustents else 'Nenhum'}")
print(f"Meios de Locomoção Não Sustentáveis: {', '.join(nsustents) if nsustents else 'Nenhum'}")
print(f"   ➜ Situação: {situation}")
print("=" * 60)

os.system("pause")
