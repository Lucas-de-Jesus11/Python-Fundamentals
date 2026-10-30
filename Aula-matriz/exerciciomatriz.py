#Faça um programa que oeça as quatro notas de 6 alunos, calcule e armazene num vetor a média de cada aluno
#imprima o número de alunos com média maior ou igual a 7.0
matriz = []
print('Preencha uma matriz 6x4')
for i in range(6):
    linha = []
    for j in range(4):
        valor = int(input(f'Digite as notas do [{i}][{j}]º aluno: '))
        linha.append(valor)
    matriz.append(linha)
print('Matriz: ')
for linha in matriz:
    print(linha)
