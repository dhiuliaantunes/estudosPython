#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  exercicio11.py
#  
#  Copyright 2022 HDN <HDN@LAPTOP-P3D340I9>
#  
#Faça um algoritmo para ler o salário de um funcionário e aumentá-Io em
#15%. Após o aumento, desconte 8% de impostos. Imprima o salário inicial, o
#salário com o aumento e o salário final.

salario = float(input("Informe o salário: "))

salarioAumento = salario*1.15
salarioFinal = salarioAumento - (salarioAumento*0.08)

print("\nSalário inicial: ", salario)
print("Salário com aumento: ", salarioAumento)
print("Salário final: ", salarioFinal)
