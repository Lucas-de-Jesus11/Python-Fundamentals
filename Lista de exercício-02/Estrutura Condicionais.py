#Exercicío 1
#Faça um algoritmo para ler dois números inteiros diferentes e escrever o maior.
'''n1 = int(input('Primeiro número: '))
n2 = int(input('Segundo número: '))
if n1 >= n2 :
  print(f'{n1} é o maior')
else:
  print(f'{n2} é maior')'''

#Exercício 2
#Tendo como dados de entrada a altura e o sexo de uma pessoa (M = masculino e F = feminino),
#construa um programa que calcule seu peso ideal, utilizando as seguintes fórmulas:
#Para homens: (72.7 * h) - 58
#Para mulheres: (62.1 * h) - 44.7
'''altura = float(input('Altura: '))
sexo = str(input('Sexo: (M para masculino, F para feminino): ')).upper()
if sexo == 'M':
  peso_ideal = (72.7 * altura) - 58
  print(f'Peso ideal: {peso_ideal:.2f}Kg')
elif sexo =='F':
  peso_ideal = (62.1 * altura) - 44.7
  print(f'Peso ideal: {peso_ideal:.2f}')
else:
  print('Sexo inválido! Por favor, digite M para masculino ou F para feminino.')'''

# Exercício 3
#Faça um programa que leia a idade de uma pessoa e verifique se ela é:
#Criança: Idade de 1 a 13 anos;
#Adolescente: Idade maior que 13 anos e menor ou igual a 20 anos;
#Adulto: Idade maior que 20 e menor ou igual a 50 anos;
#Idosa: idade maior que 50 anos.
'''idade = int(input('Digite sua idade: '))
if idade <= 13:
  print('Criança')
elif idade >= 13 and idade <= 20:
  print('Adolecente')
elif idade >= 20 and idade <= 50:
  print('Adulto')
else:
  print('Idosa')'''

#Exercício 4
#Fazer um programa para calcular o salário líquido de um funcionário com base na seguinte fórmula:
#salário líquido = salário bruto + proventos - desconto
#Devem ser respeitadas as seguintes condições para cálculo do desconto:
#Salário Bruto <= R$5000, desconto de 5%
#Salário Bruto > R$5000, desconto de 10%
'''salario_bruto = float(input('Salário bruto: R$'))
proventos = float(input('Proventos:'))
if salario_bruto <= 5000:
  desconto =  salario_bruto * 0.05
else:
  desconto = salario_bruto * 0.10
salario_liquido = salario_bruto + proventos - desconto
print(f'Salário liquido: R${salario_liquido:.2f}')'''

#Exercício 5
#Determine se um determinado ano lido é bissexto.
#Sendo que um ano é bissexto se for divisível por 400 ou se for divisível por 4 e não for divisível por 100.
'''from datetime import date
ano = int(input('Que ano quer analisar? Coloque 0 para analisar o ano atual: '))
if ano == 0:
  ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
  print(f'O ano {ano} é BISSEXTO')
else:
  print(f'O ano {ano} não é bissexto')'''