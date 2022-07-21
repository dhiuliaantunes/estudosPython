#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  exercicio4.py
#  
#  Uma empresa de desenvolvimento de software cobra anuidades pelas licenças do seu sistema.
#  Atualmente, esse valor é de R$ 20.000.00 por ano mas, devido a inflação, esse valor tem subido 4% a cada ano. 
#  Faça um programa que simule o valor dessa anualidade durante os próximos 10 anos;
#  Modifique o programa anterior para que seja o usuário que informe qual é a taxa de inflação que deve ser aplicada a cada ano;
#  
#  
for i in range(10):
	print(20000*((1 + 0.04)**i))
	i = i + 1
