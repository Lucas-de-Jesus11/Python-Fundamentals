#Faça um programa que peça dois números ao usúario e mostre qual o maior e qual o menor

#Solicita dois números ao usuário
numero1 = int(input('Digite o primeiro número: '))
numero2 = int(input('Digite o segundo número: '))

#Verifica qual número é o maior e qual o menor
if numero1 > numero2:
    print(f'O maior númeero é: {numero1}')
    print(f'O menor númeero é: {numero2}')
elif numero1 < numero2:
    print(f'O maior número é: {numero2}')
    print(f'O menor número é: {numero1}')
else:
    print('Os dois números são iguais.')

