n = 1
pares = 0
impares = 0
somaP = 0
somaI = 0


while(n > 0):
	n = int(input("Informe um número inteiro: "))
	if n%2==0:
		pares = pares + 1
	else:
		impares = impares + 1
		
print("\nQuantidade de pares: ", pares)

print("\nQuantidade de ímpares: ", impares)
