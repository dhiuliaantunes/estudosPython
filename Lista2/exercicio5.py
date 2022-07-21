#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  exercicio5.py
#  
#  Copyright 2022 HDN <HDN@LAPTOP-P3D340I9>
#  
# Construa um algoritmo que, dado o primeiro elemento e a razão de uma progressão aritmética (PA) [link],
# imprima todos os n primeiros elementos da PA, onde n também é informado pelo usuário. 
# Lembre-se que uma PA pode ser crescente ou decrescente. 

elemento = int(input("Informe o primeiro elemento da PA:\n"))
razao = int(input("\nInforme a razão da PA:\n"))
n = int(input("\nInforme a quantidade de elementos que a PA deve rotornar:\n"))
i = 1

print(elemento)
print(razao)
while i <= n:
	paN = elemento+(razao*(n-1))
	print(paN)
	
	i = i + 1
	elemento = paN
