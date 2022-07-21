#Na eleição para coordenação de curso, existem 3 candidatos.
#Os votantes podem digitar 1, 2 ou 3 para escolher um dos candidatos; 
#4 para votar em branco; 5 para votar nulo. 
#A votação se encerra quando o fiscal digitar 0 (zero).
#Escreva um algoritmo que mostre 
#O número do candidato vencedor; 
#O número de votos em branco; 
#O número de votos nulos;
#O número de eleitores que compareceram às urnas. 

v = 6
c1 = 0
c2 = 0
c3 = 0
branco = 0
nulo = 0

while(v != 0):
	v = int(input("\nVoto: "))
	if(v == 1):
		c1 = c1 + 1
	
	elif(v == 2):
		c2 = c2 + 1
		
	elif(v == 3):
		c3 = c3 + 1
	
	elif(v == 4):
		branco = branco + 1
	
	elif(v == 5):
		nulo = nulo + 1
	else:
		if(v != 0):
			print("\nVoto inválido")
		
if(c1 > c2) and (c1 > c3) and (c1 > branco) and (c1 > nulo):
	print("\nCandidato 1 é o vencedor.")
		
elif(c2 > c1) and (c2 > c3) and (c2 > branco) and (c2 > nulo):
	print("\nCandidato 2 é o vencedor.")	

elif(c3 > c1) and (c3 > c2) and (c3 > branco) and (c3 > nulo):
	print("\nCandidato 3 é o vencedor.")	

else:
	print("\nHouve um empate.")
	
print("\nQuantidade de votos em branco: ", branco)
print("\nQuantidade de votos nulos: ", nulo) 
