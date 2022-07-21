#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  exercicio6.py
#  
#  Copyright 2022 HDN <HDN@LAPTOP-P3D340I9>
#  
#Escreva um algoritmo que tenha como entrada do usuário o peso (M), em kg, e a
#altura (H), em m, de uma pessoa e que calcule o seu IMC a partir da fórmula:
#IMC = M/H²
#Teste:
#M = 72 H = 1,7 IMC = 24,91

m = float(input("Informe o peso(kg): "))

h = float(input("\nInforme a altura(m): "))

print("\nO IMC é: ", m/(h**2))
