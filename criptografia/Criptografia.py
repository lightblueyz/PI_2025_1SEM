import sympy
from sympy import Matrix


def clear():
    from os import system as sys

    sys("cls")


clear()

ALFABETO = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
CHAVE = Matrix([[3, 2], [4, 1]])


def texto_para_numeros(texto):
    texto = str(texto)
    texto = texto.upper()
    return [ALFABETO.index(char) for char in texto if char in ALFABETO]


def numeros_para_texto(numeros):
    return "".join([ALFABETO[n % 26] for n in numeros])


def Cypher(texto):
    numeros = texto_para_numeros(texto)
    if len(numeros) % 2 != 0:
        numeros.append(ALFABETO.index("X"))
    resultado = []
    for i in range(0, len(numeros), 2):
        bloco = Matrix([[numeros[i]], [numeros[i + 1]]])
        matrizCripto = CHAVE * bloco
        resultado.extend([int(x) % 26 for x in matrizCripto])
    return numeros_para_texto(resultado)


def Decypher(texto):
    numeros = texto_para_numeros(texto)
    chaveInversa = CHAVE.inv_mod(26)
    resultado = []
    for i in range(0, len(numeros), 2):
        bloco = Matrix([[numeros[i]], [numeros[i + 1]]])
        matrizDescripto = chaveInversa * bloco
        resultado.extend([int(x) % 26 for x in matrizDescripto])
    descriptografado = numeros_para_texto(resultado)

    if descriptografado.endswith("X"):
        descriptografado = descriptografado[:-1]
    try:
        return int(descriptografado)
    except:
        return descriptografado


