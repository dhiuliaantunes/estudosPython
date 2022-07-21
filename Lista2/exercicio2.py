#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  exercicio2.py
#  
#  Copyright 2022 HDN <HDN@LAPTOP-P3D340I9>
#  

#Fulano comprou um saco de ração com peso em quilos. Ele possui dois cachorros, para os quais fornece 
#a quantidade de ração em gramas. A quantidade diária de ração fornecida para cada cachorro é sempre a mesma. 
#Faça um programa que receba o peso do saco de ração e a quantidade de ração fornecida para cada cachorro (em gramas),
#e calcule e mostre quanto restará de ração no saco após cinco dias (em gramas).

peso = float(input("Informe o peso(kg) do pacote de ração: "))
qtde = float(input("\nInforme a quantidade diária fornecida a cada cachorro: "))

pesoG = peso * 1000
resto = pesoG - (qtde*10)

print("\nApós 5 dias, a quantidade(g) restante de ração será de: ") 

if resto >= 1000:
	print(resto/1000, "kg")
else:
	print(resto, "g")
