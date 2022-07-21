#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  exercicio2

#Escreva um algoritmo que calcule e mostre quantos pneus será necessário para x
#carros, sendo x informado pelo usuário, e o valor necessário para a compra sendo
#que cada pneu custa R$ 275,00.
#Teste: para 10 carros, 40 pneus, R$ 11000

x = int(input("Informe a quantidade de carros: "))

print()
print("Serão necessários ", x * 4, "pneus")
print()
print("O custo total será de R$ ", (x * 4) * 275)
