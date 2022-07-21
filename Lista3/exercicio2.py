#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  exercicio2.py
#  
#  Copyright 2022 HDN <HDN@LAPTOP-P3D340I9>
#  

n = int(input("Informe um número inteiro: "))
div = 0
palavra = "palavra"

print(palavra)

for i in range(1, n+1):
	if n%i==0:
		div = div + 1
	else:
		div = div
	
print("Divisores de n: ", div)

