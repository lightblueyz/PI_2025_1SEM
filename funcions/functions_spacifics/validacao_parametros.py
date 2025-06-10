def litros_val():
    while True:
        try:
            Litros = float(input("Quantidade de Água gasta (L): "))
            return Litros
        except ValueError:
            print("Entrada inválida. Digite apenas valores numéricos!")


def kwh_val():
    while True:
        try:
            KWh = float(input("Quantidade de Energia Elétrica (kWh): "))
            return KWh
        except ValueError:
            print("Entrada inválida. Digite apenas valores numéricos!")


def kgn_val():
    while True:
        try:
            Kgn = float(input("Quantidade de Resíduos não recicláveis (Kg): "))
            return Kgn
        except ValueError:
            print("Entrada inválida. Digite apenas valores numéricos!")


def kgr_val():
    while True:
        try:
            Kgr = float(input("Quantidade de Resíduos recicláveis (Kg): "))
            return Kgr
        except ValueError:
            print("Entrada inválida. Digite apenas valores numéricos!")
