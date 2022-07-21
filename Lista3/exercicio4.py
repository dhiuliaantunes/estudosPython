#soma = 0

#for i in range(4):
#	n = float(input("Informe a nota: "))
#	soma = soma + n
	
#media = soma / 4
#print("A média das notas é: ", media)

n1 = float(input("\nInforme a nota de Português: "))
n2 = float(input("\nInforme a nota de Inglês: "))
n3 = float(input("\nInforme a nota de Conhecimentos específicos: "))
n4 = float(input("\nInforme a nota de Legislação: "))

media = (n1 + n2 + n3 + n4)/4
mediaP = ((n1 * 2.5) + (n2 * 2.5) + (n3 * 3) + (n4 * 2)) / 10

print("\nMédia aritmética: ", media)
print("\nMédia ponderada: ", mediaP)
