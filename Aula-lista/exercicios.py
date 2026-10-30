# 1- Faça um programa que leia um vetor de 5 numeros inteiros e mostre-os
'''
numeros = []
for i in range(5):
    numero = int(input(f'Digite o {i+1}º número: '))
    numeros.append(numero)
print('Os números digitados são: ')
for numero in numeros:
    print(numero, end='-')
'''

# 2- Faça um programa que leia um vetor de 10 numeros reais e mostro-os na ordem inversa
'''
numeros = []
for i in range (10):
    numero = int(input(f'Digite o {i+1}º número: '))
    numeros.append(numero)
print('Os números digitados na ordem inversa são: ')
for numero in reversed(numeros):
    print(numero, end='-')
'''

# 3- Faça um programa que leia 4 notas, mostre as notas e a média na tela
'''
notas = []
for i in range(4): 
    num = float(input(f'Digite a {i+1}º nota:'))
    notas.append(num)
qtd = len(notas)
média = sum(notas) / qtd
print('\nNotas digitadas: ')
for i, nota in enumerate(notas, 1):
    print(f'Nota {i}: {nota:.1f}')
print(f'\nA média das notas é: {média:.1f}')
'''

# 4- Faça um programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas, imprima as consoantes

# 5- Faça um Programa que leia 20 números inteiros e armazene-os num vetor.
#Armazene os números pares no vetor PAR e os números IMPARES no vetor impar.
#Imprima os três vetores.
'''num = list()
pares = []
impares = []
for i in range(20):
    numeros = int(input(f'Digite o {i+1}º: '))
    num.append(numeros)
    if numeros % 2 == 0:
        pares.append(numeros)
    else:
        impares.append(numeros)

num.sort()
pares.sort()
impares.sort()

print(f'\nNúmeros inseridos: {num}')
print(f'Os números pares são: {pares}')
print(f'Os números impares são: {impares}')
'''

#6- Faça um Programa que leia um vetor de 5 números inteiros, mostre a soma, a multiplicação e os números
'''
num = list()
produto = 1
for i in range(5):
    numeros = int(input(f'Digite o {i+1}º: '))
    num.append(numeros)
print(f'A soma dos valores é: {sum(num)}')
for n in num:
    produto *= n
print(f'O produtos dos números é: {produto}')
'''