#Exercicio 1
#Faça um algoritmo para ler um número inteiro e informar se este é menor, maior ou igual 10.
"""num = int(input('Digite um número: '))
if num < 10:
    print(f'O número {num} é menor que 10')
elif num == 10:
    print(f'O número {num} é igual a 10')
elif num > 10:
    print(f'O número {num} é maior que 10')"""

#Exercício 2
#Crie um algoritmo para ler dois números inteiros e informar se estes números são iguais ou diferentes.
"""n1 = int(input('Primeiro número: '))
n2 = int(input('Segundo número: '))
if n1 == n2:
    print('São iguais!')
elif n1 != n2:
    print('São diferentes!')"""

#Exercício 3
#Faça um algoritmo para ler um número inteiro e informar se o número é par ou ímpar.
"""numero = int(input('Digite um número para saber se é par ou impar: '))
resultado = numero % 2
if resultado == 0:
    print(f'O {numero} é PAR')
else:
    print(f'O {numero} é IMPAR')"""

#Exercício 4
#Faça um algoritmo para ler dois números inteiros A e B e informar se A é divisível por B.
"""A = int(input('Primeiro número: '))
B = int(input('Segundo número: '))
if A % B == 0:
    print(f'{A} é divisivel por {B}')
elif A / B:
    print(f'{A} não é divisel por {B}')"""
# Leitura dos números A e B
A = int(input("Digite o valor de A: "))
B = int(input("Digite o valor de B: "))

# Verificação se B é zero
'''if B == 0:
    print("Divisão por zero não é permitida.")
else:
    # Verificação da divisibilidade
    if A % B == 0:
        print("A é divisível por B.")
    else:
        print("A não é divisível por B.")'''

#Exercício 5
#Modifique o programa do exercício 4, adicione uma condicional para impedir que o segundo número seja zero.
#Neste caso, imprima: “impossível dividir N por zero!”, onde N é o primeiro número digitado.
'''A = int(input('Primeiro número: '))
B = int(input('Segundo número: '))
if B == 0:
  print(f'Impossivel dividir {A} por zero!')
else:
    if A % B == 0:
        print(f'{A} é divisivel por {B}')
    elif A / B:
        print(f'{A} não é divisel por {B}')'''