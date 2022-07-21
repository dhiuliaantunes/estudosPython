#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  exercicio3.py
#  
#  Copyright 2022 HDN <HDN@LAPTOP-P3D340I9>
#  
#Um banco concederá um crédito especial aos seus clientes, variável com o saldo médio no último ano. 
#Faça um algoritmo que leia o saldo médio de um cliente e calcule o valor do crédito de acordo com a tabela abaixo.
#Mostre uma mensagem informando o saldo médio e o valor do crédito.

saldo = float(input("Informe o saldo médio:\n"))

if saldo <= 200:
	print("Saldo não considerado para crédito.")

if saldo >= 201 and saldo <= 400:
    print("O crédito será de: ", saldo*0.2)
    
if saldo >= 401 and saldo <= 600:
    print("O crédito será de: ", saldo*0.3)  
    
if saldo >= 601:
    print("O crédito será de: ", saldo*0.4)



