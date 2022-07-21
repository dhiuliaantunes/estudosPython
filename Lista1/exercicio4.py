#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  exercicio4.py
#  
#  Copyright 2022 HDN <HDN@LAPTOP-P3D340I9>
#  

#Escreva um algoritmo que troque o valor de 2 variáveis, a e b, de modo que, no fim
#da execução, b possua o valor de a e vice-versa. Mostre na tela os valores antes e
#depois da troca;
#Teste:
#Antes: a=5, b=7
#Depois: a=7, b=5
#

a = 5
b = 7
print(a, b)
 
c = a
a = b
b = c

print(a, b)

