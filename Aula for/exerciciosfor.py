#Entrar com sexo de várias pessoas e imprimir quantas pessoas são do sexo masculino(considerar m ou M)

# Lista para armazenar os sexos
'''sexos = []

# Número de entradas
n = int(input("Quantas pessoas você deseja cadastrar? "))

# Coletar os sexos
for i in range(n):
    sexo = input(f"Digite o sexo da pessoa {i + 1} (m/M para masculino, f/F para feminino): ")
    sexos.append(sexo)

# Contar quantas pessoas são do sexo masculino
masculinos = sum(1 for s in sexos if s.lower() == 'm')

print(f"Total de pessoas do sexo masculino: {masculinos}")
'''

#1-Encontrar todos os números pares entre 1 e 100
'''for cont in range(2, 102, 2):
#  if cont % 2 == 0:
    print(cont, end=' ')
print('Acabou')
'''

#2-Faça um programa que leia 5 números e informe a soma e a média dos números:
'''s = 0 
média = 0
for c in range(1, 6):
    n = int(input(f'Digite o {c}º número: '))
    s += n 
    média = s / n
print(f'O somatório dos valores é {s} e a média é {média:.1f}')
'''

#3-Faça um programa que peça para n pessoas a sua idade, ao final o programa deverá verificar se a média de idade da turma varia entre:
#0 e 25,26 e 60 e maior que 60 e então;
#dizer se a turma é jovem, adulta ou idosa, corforme a média calculada

#4-Numa eleição existem três candidatos:
#Faça um programa que peça o número total de eleitores. Peça para cada eleitor votar e ao final
#mostrar o número de votos de cada candidato.

#5-Escreva um programa que mostre todos os números entre 5 e 100 que são divisíveis por 7, mas não são múltiplos de 5. Os números obtidos devem ser impressos em sequência.   

#6-Ler do teclado a idade e o sexo de 10 pessoas, calcule e imprima:
#idade média das mulheres
#idade média dos homens
#idade média do grupo
idade = 0
sexo = 0
contador = 0
for i in range(1, 11):
    p = int(input(f'Informe a idade e o sexo da {i}º pessoa: '))
    sexo = int(input('Sexo: '))
    

#7-Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.

