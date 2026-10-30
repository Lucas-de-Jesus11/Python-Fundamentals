#Programa que contenha dados inicias (nome,sobrenome,idade).Depois que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.Calcule a mostre o total do seu salário no referido mês.
nome_e_sobrenome = (input('Digite seu nome e sobrenome: '))
idade = int(input('Coloque sua idade: '))
salario = float(input('Quanto você ganha por hora: '))
horas = float(input('Qual o número de horas trabalhadas por mês: '))
total = salario * horas
print(f'O total de seu saláro é de R$: {total}')