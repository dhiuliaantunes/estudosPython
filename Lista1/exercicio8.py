#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  exercicio8.py
#  
#  Copyright 2022 HDN <HDN@LAPTOP-P3D340I9>
#  
#Uma fábrica de camisetas produz os tamanhos pequeno, médio e grande, cada uma
#sendo vendida respectivamente por 10, 12 e 15 reais. Construa um algoritmo em que
#o usuário forneça a quantidade de camisetas pequenas, médias e grandes referentes
#a uma venda, e o algoritmo informe quanto será o valor arrecadado.
#Teste:
#P = 1 , M = 2 , G = 3
#total = 79 reais
#  
#  

p = int(input("Informe a qtde de camisetas de tamanho P: "))

m = int(input("\nInforme a qtde de camisetas de tamanho M: "))

g = int(input("\nInforme a qtde de camisetas de tamanho G: "))

print("\nO total(R$) será de: ", (p*10) + (m*12) + (g*15)) 
