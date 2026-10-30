#cadastramento de (nome, sobrenome,idade, RA) peça as 4 notas bimestrais e mostre a média
nome_sobrenome = input('Digite seu nome e sobrenome: ')
idade = int(input('Coloque sua idade: '))
RA = int(input('Informe seu RA: '))
n1 = float(input('Digite sua primeira nota: '))
n2 = float(input('Digite sua segunda nota: '))
n3 = float(input('Digite sua terceira nota: '))
n4 = float(input('Digite sua quarta nota: '))
média = (n1 + n2 + n3 + n4) / 4
print(f'Seu nome e sobrenome é {nome_sobrenome} e você tem {idade} anos!')
print(f'Sua média entre {n1:.1f}, {n2:.1f}, {n3:.1f} e {n4:.1f} é igua a {média:.1f}')