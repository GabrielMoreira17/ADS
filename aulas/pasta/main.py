# 1 - Escreva um programa que receba o raio de uma esfera como entrada
#  e produza o diâmetro, a circunferência, a área da superfície e o volume da esfera.
# Formula: diametro = 2 * raio
# Circunferência = diametro * PI
# areaSuperficie = 4 * PI * raio^2
# Volume = 4/3 * PI * raio^3

from math import pi

raio = int(input('Digite o raio do circulo: '))
diametro = 2 * raio
circunferencia = diametro * pi
areaSuperficie = 4 * pi * (raio*raio)
volume = 4/3 * pi * raio**3

print(f'o diametro é: {diametro}, a circunferência é {circunferencia}, a área da superfície é {areaSuperficie} e o volume é {volume}')



# 2 - Sabendo que a média de aprovação é 7 e a formula para cálculo da média é: Média = (N1 + N2*2)/3
# Realize o algoritmo que calcule quanto deve ser a nota da segunda avaliação para que o resultado do aluno seja a aprovação.

n1 = float(input("Digite a nota da primeira avaliação: "))

media_aprovacao = 7

n2 = ((media_aprovacao * 3) - n1) / 2

print("A nota necessária na segunda avaliação é:", n2)


# 3- Cardapio da lanchonete e soma do gasto total

Hamburguer = 3
Cheesburguer = 2.50
fritas = 2.50
refrigerante = 1
milkshake = 3

qtdHamburguer = int(input('Digite a quantidade de Hamburguer'))
qtdCheesburguer = int(input('Digite a quantidade de cheesburguer'))
qtdFritas = int(input('Digite a quantidade de fritas'))
qtdRefrigerantes = int(input('Digite a quantidade de refrigerantes'))
qtdMilkShake = int(input('Digite a quantidade de milkshake'))

calculo = (Hamburguer * qtdHamburguer) + (Cheesburguer * qtdCheesburguer) + (fritas * qtdFritas) + (refrigerante*qtdRefrigerantes) + (milkshake * qtdMilkShake)

print(calculo)