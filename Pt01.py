#Projeto integrador eng de software 2025
#by: Tomás Toniato, Pedro André, Guilherme Preventi, Daniel Honorato e Diogo


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

Litros = float(input(" Quantidade de Água gasta (L): "))
KWh = float(input(" Quantidade de Energia Elétrica (kWh): "))
Kgn = float(input(" Quantidade de Resíduos não recicláveis gerados (Kg): "))
Kgr = float(input(" Quantidade de Resíduos recicláveis gerados (Kg): "))


Tp = int(input(" Você utilizou transporte publico hoje? Sim(1)Não(0): ")) #Sustentavel
Bk = int(input(" Você utilizou bicicleta hoje? Sim(1)Não(0): ")) #Sustentavel
Cm = int(input(" Você caminhou até o seu destino hoje? Sim(1)Não(0): ")) #Sustentavel
Cr = int(input(" Você utilizou carro comum hoje? Sim(1)Não(0): ")) 
Cre =int(input(" Você utilizou carro elétrico hoje? Sim(1)Não(0): ")) #Sustentavel
Crn =int(input(" Você utilizou de carona hoje? Sim(1)Não(0): "))


sustents = []
nsustents = []

sust = ""
sustn = ""



if Tp == 1 or Bk == 1 or Cm == 1 or Cre == 1:
    sust = True
else: 
    sust = False
    
if Tp == 1:
    sustents.append("Transporte Público")
if Bk == 1:
    sustents.append(", Bicicleta")
if Cm == 1:
    sustents.append(", Caminhada")
if Cre == 1:
    sustents.append(", Carro Elétrico")        
        
          
    
if Cr == 1 or Crn == 1:
    sustn = True
else: 
    sustn = False            

if Cr == 1:
    nsustents.append("Carro Comun")
if Crn == 1:
    nsustents.append("Carona")


situation = ""



if sustn == 1 and sust == 1:
  situation = ("🟡 Sustentabilidade Moderada")
elif sustn == 1 and sust == 0:
  situation = ("🔴 Baixa Sustentabilidade")
elif sustn == 0 and sust == 1:
  situation = ("🟢 Alta Sustentabilidade")

if Kgr != 0 and Kgn != 0:
  soma = Kgr + Kgn
  porc = (Kgn * 100) / soma





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
print(f"   ➜ Situação: {situacaoporc}\n")
print(f" Meios de locomoção: {sustents, nsustents}")
print(f"   ➜ Situação: {situation}")
print("=" * 50)



os.system("pause")