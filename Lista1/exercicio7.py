#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  exercicio7.py
#  
#  Copyright 2022 HDN <HDN@LAPTOP-P3D340I9>
#  
#Escreva um algoritmo que receba um valor em reais do usuário, e mostre o valor em
#reais, o valor em dólares e o valor em euro.
#Cotação do dólar em 04/03 às 17:04h = 4.58 reais
#Cotação do euro em 04/03 às 17:04h = 5.1 reais

v = int(input("Informe o valor em reais a ser convertido: "))

print("\nValor convertido em dólar: ", v/4.58)

print("\nValor convertido em euro: ", v/5.1)
