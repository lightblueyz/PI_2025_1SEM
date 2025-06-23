from sympy import Matrix


ALFABETO = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
CHAVE = Matrix([[3, 0], [2, 1]])


def letra_para_numero(letra):
    if letra == "Z":
        return 0
    else:
        return ord(letra) - ord("A") + 1


def numero_para_letra(numero):
    if numero == 0:
        return "Z"
    else:
        return chr(numero - 1 + ord("A"))


def texto_para_numeros(texto):
    texto = texto.upper()
    return [letra_para_numero(c) for c in texto if c in ALFABETO]


def numeros_para_texto(numeros):
    return "".join([numero_para_letra(n % 26) for n in numeros])


def Cypher(texto):
    numeros = texto_para_numeros(texto)
    if len(numeros) % 2 != 0:
        numeros.append(letra_para_numero("X"))
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
    return descriptografado


def menu():
    while True:
        print("\n=== MENU HILL CIPHER ===")
        print("1. Criptografar texto")
        print("2. Descriptografar texto")
        print("3. Sair")

        try:
            opcao = int(input("Escolha uma opção: "))
        except ValueError:
            print("Entrada inválida, digite um número.")
            continue

        if opcao == 1:
            texto = input("Digite o texto para criptografar: ")
            cripto = Cypher(texto)
            print(f"Texto criptografado: {cripto}")
        elif opcao == 2:
            texto = input("Digite o texto criptografado: ")
            decripto = Decypher(texto)
            print(f"Texto descriptografado: {decripto}")
        elif opcao == 3:
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")
menu()