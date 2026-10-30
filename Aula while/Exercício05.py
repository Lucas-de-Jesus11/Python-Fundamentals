#Faça um program em Python que leia n números inteiros a partir do teclado, até que o usuário digite 0. Ao final, mostre a soma de todos os números digitados
'''
total = 0
while True:
    numero = int(input('Digite um número inteiro (digite 0 para parar): '))
    if numero == 0:
        break
    total += numero
print(f'A soma de todos os número é {total}')
'''
contador = 0
numero = 1
soma = 0
while numero != 0:
    numero= int(input(f'Digite um número {contador+1}: '))
    if numero == 0:
        break
    contador += 1
    soma += numero
print(f'A soma dos numeros digitados é {soma}')
