import os
import time
from db.server import conn, cursor
from datetime import datetime
from funcions.post import cadastro
from funcions.get import listar
from funcions.get_media import get_media
from funcions.delete import delete
from funcions.put import alterar_registro  


def what_more():
    while True:
        try:
            loop = int(input("Deseja algo mais? (1)SIM | (2)NÃO: "))
            if loop in [1, 2]:
                return loop
            else:
                print("Opção inválida. Digite 1 para SIM ou 2 para NÃO.")
        except ValueError:
            print("Entrada inválida. Digite um número (1 ou 2).")


def getDtTm():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


while True:
    os.system("cls")
    print("-" * 50)
    print("BEM-VINDO AO MENU DE SUSTENTABILIDADE")
    print("1-Cadastro de parâmetros diários de sustentabilidade")
    print("2-Alteração de parâmetros diários de sustentabilidade")
    print("3-Exclusão de parâmetros de sustentabilidade")
    print("4-Listagem de Parâmetros")
    print("5-Média geral dos dados")
    print("6-Sair")

    try:
        opcao = int(input("Digite a opção que deseja: "))
    except ValueError:
        print("Por favor, digite um número válido.")
        time.sleep(2)
        continue

    if opcao == 1:
        os.system("cls")
        date = getDtTm()
        cadastro(date)

    elif opcao == 2:
        os.system("cls")
        alterar_registro()  
        time.sleep(3)

    elif opcao == 3:
        os.system("cls")
        delete()
        time.sleep(3)

    elif opcao == 4:
        os.system("cls")
        listar()
        time.sleep(3)

    elif opcao == 5:
        os.system("cls")
        get_media()
        time.sleep(3)

    elif opcao == 6:
        os.system("cls")
        print("Deseja sair?")
        sair = what_more()
        if sair == 2:
            os.system("cls")
            print("Obrigado, até a próxima!")
            time.sleep(3)
            break
        else:
            os.system("cls")
            continue

    else:
        print("*Opção Inválida*")
        time.sleep(2)
        continue

    continuar = what_more()
    if continuar == 2:
        os.system("cls")
        print("Obrigado, até a próxima!")
        time.sleep(3)
        break
    else:
        os.system("cls")

cursor.close()
conn.close()
