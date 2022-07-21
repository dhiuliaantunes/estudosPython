n = int(input("Informe um número inteiro: "))
div = 0

for i in range(1, n+1):
	if n%i==0:
		div = div + 1
	else:
		div = div

if div > 2:
	print("Esse número não é primo.")
else:
	print("Esse número é primo.")
