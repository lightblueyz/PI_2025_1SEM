import os
from datetime import datetime


os.system("cls") 



def getDtTm():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

print("=" * 50)
print(f"{' ANÁLISE DE SUSTENTABILIDADE ':^50}")
print("=" * 50)
print(f"Data e Hora: {getDtTm()}")
print("=" * 50)


Dias = int(input("\n Digite o período analisado (em dias): "))
Litros = float(input(" Quantidade de Água gasta (L): "))
KWh = float(input(" Quantidade de Energia Elétrica (kWh): "))
Kgn = float(input(" Quantidade de Resíduos não recicláveis (Kg): "))
Kgr = float(input(" Quantidade de Resíduos recicláveis (Kg): "))
soma = Kgr + Kgn

porc = (Kgn * 100) / soma

Litros = Litros / Dias
KWh = KWh / Dias





def avaliar(valor, baixo, moderado):
    if valor < baixo:
        return("🟢 Alta Sustentabilidade")
    elif baixo <= valor <= moderado:
        return("🟡 Sustentabilidade Moderada")
    else:
        return("🔴 Baixa Sustentabilidade")

situacaolitros = avaliar(Litros, 150, 200)
situacaoporc = avaliar(porc, 20, 50)
situacaokwh = avaliar(KWh, 5, 10)


print("\n" + "=" * 50)
print(f" Quantidade de Água gasta por dia: {Litros:.2f} L")
print(f"   ➜ Situação: {situacaolitros}\n")
print(f" Quantidade de Energia gasta por dia: {KWh:.2f} kWh")
print(f"   ➜ Situação: {situacaokwh}\n")
print(f" Porcentagem de resíduos não recicláveis: {porc:.2f} %")
print(f"   ➜ Situação: {situacaoporc}")
print("=" * 50)
