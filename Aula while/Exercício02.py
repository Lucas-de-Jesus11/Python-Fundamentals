#Faça um programa que calcule e mostre a média aritmética de N notas
notas = 0 
qtd_notas = 0
while True:
    nota = float(input('Informe a nota: '))
    if nota == 1:
        break
    notas += nota
    qtd_notas += 1
if qtd_notas > 0:
    media = notas / qtd_notas
    print(f'Quantidade de notas informadas {qtd_notas}')
    print(f'Média das notas: {notas / qtd_notas:.2f}')
else:
    print('Nenhuma nota informada!')