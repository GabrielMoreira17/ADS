from math import pi, sqrt, pow

# Faça um programa que leia um número inteiro e o imprima.

numero = int (input('Digite um número: '))
print(numero)


# Faça um programa que leia um número real e o imprima.

numero = float (input('Digite um número: '))
print(numero)


# Peça ao usuário para digitar três valores inteiros e imprima a soma deles.

numero1 = int(input('Digite o primeiro número: '))
numero2 = int(input('Digite o segundo número: '))
numero3 = int(input('Digite o terceiro número: '))
soma = numero1 + numero2 + numero3
print('A soma dos três números é', soma)


# Leia um número real e imprima o resultado do quadrado desse número.

numero = int(input('Digite um número: '))
resultado = numero * numero
print(resultado)


# Leia um número real e imprima a quinta parte deste número.

numero = int(input('Digite um número qualquer: '))
quintaParte = numero / 5
print(quintaParte)


# Faça a leitura de três valores e apresente como resultado a soma dos quadrados dos três números lidos

numero1 = int(input('Digite um número: '))
numero2 = int(input('Digite um número: '))
numero3 = int(input('Digite um número: '))

ResultadoN1 = numero1 * numero1
ResultadoN2 = numero2 * numero2
ResultadoN3 = numero3 * numero3
print(ResultadoN1 + ResultadoN2 + ResultadoN3)


# Leia uma velocidade em km/h (quilômetros por hora) e apresente-a convertida em m/s (metros por segundo). 
# A fórmula de conversão é: 𝑀=𝐾3.6, sendo 𝐾 a velocidade em km/h e 𝑀 em m/s.

Km = int(input('Digite a velocidade em Km/h: '))
conversao = Km * 3.6
print(conversao)


# Leia uma distância em milhas e apresente-a convertida em quilômetros.
# A fórmula de conversão é: 𝐾=1.61∗𝑀, sendo K a distância em quilômetros e M em milhas.

DistanciaEmMilhas = float(input('Digite a distancia em milhas: '))
conversaoKm = 1.61 * DistanciaEmMilhas
print(f"Km {conversaoKm:.3f} metros")


#Leia um ângulo em graus e apresente-o convertido em radianos. A fórmula de conversão é:

anguloEmGraus = float(input('Digite o ângulo em graus: '))
converteRadiano = anguloEmGraus * 3.14 / 180
print(converteRadiano)


# 11.Uma empresa de piscinas precisa saber qual o volume em que cada piscina terá em M³, 
# sendo que o usuário irá informar a largura, comprimento e profundidade.

largura = int(input('Digite a largura da piscina: '))
comprimento = int(input('Digite o comprimento da piscina: '))
profundidade = int(input('Digite a profundidade da piscina: '))

volume = largura * comprimento * profundidade
print('O volume em  M³ é: ', volume)


# Leia um valor em reais (R$) e a cotação do dólar. Em seguida, imprima o valor correspondente em dólares.

valorEmReais = float(input('Digite o valor em Reais: '))
valorEmDolar = valorEmReais * 5.70
print(valorEmDolar)


# Leia um número inteiro e imprima o seu antecessor e o seu sucessor.

numero = int(input('Digite um número: '))
antecessor = numero - 1
sucessor = numero + 1
print('O antecessor do', numero, 'é:', antecessor, 'e o sucessor é: ', sucessor)


# Leia um número inteiro e imprima a soma do sucessor de seu triplo com o antecessor de seu dobro.

numeroInteiro = int(input('Digite um valor: '))
Soma = numeroInteiro * 3 + 1
Soma2 = numeroInteiro * 2 - 1
Resultado = Soma + Soma2
print(Resultado)


# 15.Leia o valor do raio de um círculo e calcule e imprima a área do círculo correspondente. 
# A área do círculo é 𝜋∗𝑟𝑎𝑖𝑜², considere 𝜋=3.141592.

RaioDoCirculo = float(input('digite o raio do circulo: '))
AreaDoCirculo = pi * pow(RaioDoCirculo, 2)
print('A área é:  {AreaDoCirculo}')