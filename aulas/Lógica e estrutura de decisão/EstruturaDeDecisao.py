# Estrutura de Controles - Decisão simples
from random import randint

num = int(input('Digite um número secreto de 1 a 9: '))

if num == randint(1, 9):
    print('Parabéns você acertou!')
else:
    print('Você errou!')



# Classifica idade das pessoas
idade = int(input('Digite a sua idade: '))

if idade < 12:
    print('Você é uma criança!')

elif idade <= 18:
    print('Você é um adolescente!')

elif idade <= 60:
    print('Você é adulto!')

else:
 print('Você é um idoso')


num = int(input('Digite o primeiro número: '))
numDois = int(input('Digite o segundo número: '))

if num >= numDois:
    print('O primeiro número é maior!')
else:
    print('O segundo número é maior!')
 