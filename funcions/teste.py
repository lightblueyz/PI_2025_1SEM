sexo = input("digite o sexo: ")
idade = int(input("digite a idade: "))

def programa(sexo, idade):
	if sexo == "feminino" and idade < 25:
		print ("inválido")
	else: 
		print ("válido")

programa(sexo, idade)