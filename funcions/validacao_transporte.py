def tp_val():
    while True:
        try:
            Tp = int(input("Transporte Público? (1-Sim / 0-Não): "))
            if Tp == 1 or Tp == 0:
                return Tp
            else:
                print("Opção inválida. Digite 1 para SIM ou 0 para NÃO.")
        except ValueError:
            print("Entrada inválida. Digite um número (1 ou 0).")


def bk_val():
    while True:
        try:
            Bk = int(input("Bicicleta? (1-Sim / 0-Não): "))
            if Bk == 1 or Bk == 0:
                return Bk
            else:
                print("Opção inválida. Digite 1 para SIM ou 0 para NÃO.")
        except ValueError:
            print("Entrada inválida. Digite um número (1 ou 0).")


def cm_val():
    while True:
        try:
            Cm = int(input("Caminhada? (1-Sim / 0-Não): "))
            if Cm == 1 or Cm == 0:
                return Cm
            else:
                print("Opção inválida. Digite 1 para SIM ou 0 para NÃO.")
        except ValueError:
            print("Entrada inválida. Digite um número (1 ou 0).")


def cr_val():
    while True:
        try:
            Cr = int(input("Carro Comum? (1-Sim / 0-Não): "))
            if Cr == 1 or Cr == 0:
                return Cr
            else:
                print("Opção inválida. Digite 1 para SIM ou 0 para NÃO.")
        except ValueError:
            print("Entrada inválida. Digite um número (1 ou 0).")


def cre_val():
    while True:
        try:
            Cre = int(input("Carro Elétrico? (1-Sim / 0-Não): "))
            if Cre == 1 or Cre == 0:
                return Cre
            else:
                print("Opção inválida. Digite 1 para SIM ou 0 para NÃO.")
        except ValueError:
            print("Entrada inválida. Digite um número (1 ou 0).")


def crn_val():
    while True:
        try:
            Crn = int(input("Carona? (1-Sim / 0-Não): "))
            if Crn == 1 or Crn == 0:
                return Crn
            else:
                print("Opção inválida. Digite 1 para SIM ou 0 para NÃO.")
        except ValueError:
            print("Entrada inválida. Digite um número (1 ou 0).")
