#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  exercicio9.py
#  
#  Copyright 2022 HDN <HDN@LAPTOP-P3D340I9>
#  
#Um motorista deseja colocar no tanque do seu carro x reais de gasolina. Escreva um
#algoritmo para ler do usuário o preço do litro da gasolina (tipo real) e o valor total do
#pagamento, e exibir quantos litros ele conseguiu colocar no tanque.
#Teste:
#preco_litro = 4.7 , total = 100 = 21,27
#  
#  

preco = float(input("Informe o preço(litro) de gasolina: "))

valor = float(input("\nInforme o valor total de pagamento: "))

print("\nA quantidade de litros obtida será de: ", valor/preco)

