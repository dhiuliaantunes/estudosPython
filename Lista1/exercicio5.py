#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  exercicio5.py
#  
#  Copyright 2022 HDN <HDN@LAPTOP-P3D340I9>
#  
#Escreva um algoritmo para converter temperaturas em graus Celsius (inserida pelo
#usuário) para Fahrenheit e Kelvin, através das equações:
#F = 9/5C + 32 
#K = C + 273
#Teste:
#C = 20 F = 68 K = 293

c = int(input("Informe a temperatura em Celsius a ser convertida: "))

f = 9/5 * c + 32

k = c + 273

print("\nA temperatura em F é igual a: ", f)

print("\nA temperatura em K é igual a: ", k)


